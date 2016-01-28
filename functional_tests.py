from selenium import webdriver
import unittest

class NewVistorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list(self):

        self.browser.get("http://127.0.0.1:8000")
        self.assertIn('To-Do',self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1')
        self.assertIn('To-Do',header_text)

        inputbox = self.browser.find_element_by_id('new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        inputbox.send_keys('do something...')
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1:do something...' for row in rows)
        )

if __name__ == '__main__':
    unittest.main(warnings='ignore')
