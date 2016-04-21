import time
import lib.helper.captureHelper as captureHelper
from lib.perfBaseTest import PerfBaseTest


class TestSikuli(PerfBaseTest):

    def setUp(self):
        super(TestSikuli, self).setUp()
        self.test_url, self.test_url_id = self.target_helper.clone_target("1EpYUniwtLvBbZ4ECgT_vwGUfTHKnqSWi7vgNJQBemFk",
                                                                          self.env.output_name)
        time.sleep(5)
        self.sikuli.run(self.env.sikuli_path, self.env.hasal_dir, "test_chrome_switchcontentwindow",
                        self.env.test_method_name + "_" + self.env.time_stamp)

        time.sleep(3)
        captureHelper.capture_screen(self.env, self.env.video_output_sample_1_fp, self.env.img_sample_dp,
                                     self.env.img_output_sample_1_fn)

    def test_firefox_load_file(self):
        self.sikuli_status = self.sikuli.run(self.env.sikuli_path, self.env.hasal_dir, self.env.test_method_name,
                        self.env.test_method_name + "_" + self.env.time_stamp, test_url=self.test_url)
        assert(self.sikuli_status == 0)

    def tearDown(self):
        time.sleep(5)
        captureHelper.capture_screen(self.env, self.env.video_output_sample_2_fp, self.env.img_sample_dp,
                                     self.env.img_output_sample_2_fn)

        super(TestSikuli, self).tearDown()
