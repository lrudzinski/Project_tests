import pytest
import pyautogui

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_exception_interact(node, call, report):
    outcome = yield
    if report.failed:
        file_name = f"screenshot_{node.name}.png"
        pyautogui.screenshot(file_name)
        print(f"Screenshot saved as {file_name}")