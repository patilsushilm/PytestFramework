from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

driver = None
BaseUrl = "http://localhost:100"
Username = "admin"
Password = "admin"
dt = None
ExcelPath = "C:/Users/dell/PycharmProjects/vTigerPytestFramework/Files/TestData.xlsx"
SheetName = "Sheet1"


@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    # chr_options = Options()
    # chr_options.add_experimental_option("detach", True)
    # request.cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
    request.cls.driver = webdriver.Chrome()
    request.cls.driver.maximize_window()
    request.cls.driver.implicitly_wait(5)


# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     today = datetime.now()
#     report_dir = Path("vtigerreports", today.strftime("%Y%m%d"))
#     report_dir.mkdir(parents=True, exist_ok=True)
#     pytest_html = report_dir / f"Report_{today.strftime('%Y%m%d%H%M')}.html"
#     config.option.htmlpath = pytest_html
#     config.option.self_contained_html = True
#
#
# def pytest_html_report_title(report):
#     report.title = "VTiger Test Report"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    now = datetime.now()
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            # file_name = "screenshot" + now.strftime("%S%H%d%m%Y") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    now = datetime.now()
    report_dir = Path('Reports', now.strftime("%S%H%d%m%Y"))
    report_dir.mkdir(parents=True, exist_ok=True)
    pytest_html = report_dir / f"report_{now.strftime('%H%M%S')}.html"
    config.option.htmlpath = pytest_html
    config.option.self_contained_html = True


def _capture_screenshot(self, name):
    # driver.get_screenshot_as_file(name)
    self.driver.save_screenshot(name)


def pytest_html_report_title(report):
    report.title = "Automation Report"
