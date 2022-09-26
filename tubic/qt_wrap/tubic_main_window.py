import PyQt6.QtWidgets as qtw

from tubic.qt_wrap.py.main_window import MainWindowBase
from tubic.qt_wrap.workers import DownloadVideoWorker, DownloadThumbnailWorker
from tubic.yt_dlp_wrap.link_wrapper import LinkWrapper, InvalidYoutubeLinkFormat


class MainWindow(MainWindowBase):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.yt_link_wrap: LinkWrapper = LinkWrapper.get_dummy()

        self.pb_download_video.clicked.connect(
            lambda: self.try_download(
                self.yt_link_wrap.format_sort(["res:720"]), hide=self.pb_download_video
            )
        )
        self.pb_download_audio.clicked.connect(
            lambda: self.try_download(
                self.yt_link_wrap.mp3(), hide=self.pb_download_audio
            )
        )
        self.pb_abort_download.clicked.connect(self.abort_one_worker)
        self.set_status_line("ready")

    def try_download(
        self, yt_link_wrap_obj: LinkWrapper, hide: qtw.QWidget | None = None
    ):
        download_folder = qtw.QFileDialog.getExistingDirectory(self, "Select Directory")
        if download_folder:
            yt_link_wrap_obj = yt_link_wrap_obj.to(download_folder)
        else:
            return

        self.set_status_line("preparations")

        thread = DownloadVideoWorker.create_thread(self, yt_link_wrap_obj)
        if hide and hide.isVisible():
            hide.setVisible(False)
            self.pb_abort_download.setVisible(True)
            thread.finished.connect(
                lambda: [
                    hide.setVisible(True),
                    self.pb_abort_download.setVisible(False),
                ]  # a hack to run two lines in a lambda
            )
        thread.start()

    def focusInEvent(self, event) -> None:
        youtube_link: str = qtw.QApplication.clipboard().text()
        new_yt_link_wrap = None
        try:
            new_yt_link_wrap = LinkWrapper(youtube_link=youtube_link)
        except InvalidYoutubeLinkFormat as ex:
            return
        if (
            new_yt_link_wrap.video_id == self.yt_link_wrap.video_id
            and self.pb_download_video.isEnabled()
        ):
            # the user trys to replace with the same link, so ...
            return  # ... my job here is done!
        self.le_youtube_link.setText(new_yt_link_wrap.video_url)
        self.yt_link_wrap = new_yt_link_wrap

        self.set_status_line("fetching thumbnail")

        thread = DownloadThumbnailWorker.create_thread(self, self.yt_link_wrap)
        thread.start()
