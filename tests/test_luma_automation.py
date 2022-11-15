import pytest
from selenium.webdriver.common.by import By

# Создать автоматический тест по следующему сценарию:
# Открыть сайт https://magento.softwaretestingboard.com/
# Кликнуть пункт меню на Women
# Проверить, что на нужной странице


def test_go_to_tees_page(driver):
    menu_women = driver.find_element(By.LINK_TEXT, "Women")
    menu_women.click()
    assert "women" in driver.current_url, "Wrong page"


@pytest.mark.xfail
def test_go_to_tees_psge_too(driver):
    menu_women = driver.find_element(By.LINK_TEXT, "Women")
    menu_women.click()
    assert "tees" in driver.current_url, "Wrong page error"


# test comment
