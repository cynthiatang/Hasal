import os
import sys


class Sikuli():
    # hasal_dir:  DEFAULT_HASAL_DIR in environment.py
    def set_syspath(self, hasal_dir):
        library_path = os.path.join(hasal_dir, "lib", "sikuli")
        sys.path.append(library_path)
        return library_path

    # sikuli_dir: you must specify where runsikulix or runsikulix.exe is
    # hasal_dir:  DEFAULT_HASAL_DIR in environment.py
    # test_name:  test_(browser)_(test_name)
    # timestamp:  please pass in the integer generated from main python for folder record
    def run(self, sikuli_dir, hasal_dir, test_name, timestamp="", test_url=""):
        script_path = os.path.join(hasal_dir, "tests")
        if test_url == "":
            cmd = sikuli_dir + "/runsikulix -r " + script_path + "/" + test_name + ".sikuli --args " + str(
                timestamp) + " " + self.set_syspath(hasal_dir)
        else:
            cmd = sikuli_dir + "/runsikulix -r " + script_path + "/" + test_name + ".sikuli --args " + str(
                timestamp) + " " + self.set_syspath(hasal_dir) + " " + test_url
        os.system(cmd)

    def close_browser(self, browser, env):
        script_path = os.path.join(env.hasal_dir, "lib", "sikuli")
        cmd = env.sikuli_path + "/runsikulix -r " + script_path + "/closeBrowser.sikuli --args " + browser + " " + self.set_syspath(env.hasal_dir)
        os.system(cmd)

