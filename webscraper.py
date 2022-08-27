from selenium import webdriver
from selenium.webdriver.common.by import By
import textwrap

DRIVER_PATH = 'C:\\Users\\benth\\PycharmProjects\\Webscraping\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.maximize_window()
driver.get('https://www.imdb.com/title/tt0664521/')

episodes_per_season = [6, 22, 25, 14, 26, 25, 25, 24, 23]
formatted_desc = "static String[][] desc = {\n"

for i in episodes_per_season:
    formatted_desc += "{"

    for j in range(0, i):

        plot = driver.find_element(By.XPATH, '//span[@data-testid="plot-l"]')
        next_episode = driver.find_element(By.ID, "iconContext-arrow-right")
        episode_text = plot.get_attribute('innerHTML')
        sentence_list = episode_text.split('.')
        text_array = textwrap.wrap(sentence_list[0], 45)

        desc_output = ""
        for s in text_array:
            desc_output += (s + "<br>")

        desc_output = desc_output[:len(desc_output) - 4]
        formatted_desc += ('"<html>' + desc_output + '.</html>"')

        if j != i-1:
            formatted_desc += ",\n"

        if i == 23 and j == 22:
            pass
        else:
            next_episode.click()

    formatted_desc += "},\n\n"
    print(formatted_desc)


driver.quit()
formatted_desc += "};"
print(formatted_desc)
