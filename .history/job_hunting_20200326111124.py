from Scrapp_info import Jobs
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re

# indeed url only for 'morocco' jobs
global start_url
start_url = "https://ma.indeed.com"

# Options to force the window's size
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1060,810")  # right n for the width

# path for my chrome(driver)
driver = webdriver.Chrome(
    "C:\\Users\\nouamane\\Downloads\\chromedriver", options=options)

# search string
job_title = str(
    input("what job type you looking for?!! :  " + "\n" + 'job : '))

# fire (target url)
driver.get(start_url)
# time.sleep(3)
# html.send_keys(Keys.END)
# time.sleep(3)

# Switching languages
# div = driver.find_element_by_xpath('/html/body/div/div[6]/div[1]')
# p = div.find_element_by_xpath('/html/body/div/div[6]/div[1]/bidi/p')
# languages_links = []
# for i in p.find_elements_by_tag_name('a'):
#     fr_language = i.find_element_by_link_text('français')
#     fr_language.casefold()
#     if fr_language:
#         fr_href = fr_language.get_attribute('href')
#         print('french url : ', fr_href)
#         # time.sleep(3)
#         # en_href = i.find_element_by_link_text('English').click()
#     else:
#         Exception()

# associate the search with indeed search
job_field = driver.find_element_by_xpath('//*[@id="text-input-what"]')
job_field.send_keys(job_title)

global location_input
global location_field
location_field = ''
location_input = ''


def enter_clear_location():
    # Handling two cases of filtering
    location_field = driver.find_element_by_xpath(
        '//*[@id="text-input-where"]')
    try:
        if location_field == '':
            location_input = str(
                'enter location or see all available jobs ' + '\n')
            answer_me = str(
                input('yes --> give location  ||| ' + 'no --> see all'))

            print(location_input + answer_me)

            # answer is yes
            if answer_me in ('y', 'yes', 'ye'):
                ur_location = str(input('Enter location'))
                location_field.send_keys(ur_location)
                location_field.send_keys(Keys.ENTER)

            # answer == no
            if answer_me in ('n', 'no', 'nope'):
                time.sleep(2)
                location_field.send_keys(Keys.ENTER)

        # if location_field was filled (by default)
        else:
            location_field.send_keys(Keys.CONTROL + "a")
            location_field.send_keys(Keys.DELETE)
            time.sleep(2)
            location_field.send_keys(Keys.ENTER)
            time.sleep(10)

    except:
        Exception()


def sort_by():
    # Need to handle standard search and dropdown searchw²

    # Do this if (dropdown_filter) doesn't exists
    if not driver.find_elements_by_class_name('filter'):
        span_tag = driver.find_element_by_xpath(
            '//*[@id="rb_Location"]/div[1]/span')
        # div tag
        span_tag.find_element_by_xpath('//*[@id="LOCATION_rbo"]')
        # ul tag

        element = span_tag.find_element_by_xpath('//*[@id="LOCATION_rbo"]/ul')
        # li tag
        lists = element.find_elements_by_tag_name('li')
        print('all Urls available :  \n ')

        # Printing all lists of hrefs / all locations
        all_links = []
        all_locations = []
        for items in lists:
            # a tag / # Get locations name
            a_tag = items.find_element_by_tag_name('a')
            link = a_tag.get_attribute('href')
            string = a_tag.get_attribute('title')
            all_links.append(link)

            # Exclude digits whene returning titles = Locations
            new_string = ''.join(re.findall("[a-zA-Z]+", string))
            all_locations.append(new_string)

        print('urls found : ', all_links, '\n')  # optional delete later
        print('Location\'s Lists :', all_locations, '\n')

        # Convert first letter to Uppercase() if user typed it lower
        choice = input(str('Fetch results by location : \n'))
        convert_choice = (choice.title())
        if choice != convert_choice:
            location_pattern = re.compile(convert_choice)
            new_return = list(
                filter(location_pattern.match, all_locations))
            print('location after convertion is   : ', new_return)

            # return href that has input user(Location's name)
            href_pattern = re.compile('=' + convert_choice + '&jlid')
            # link match retrieved
            new_href = list(filter(href_pattern.search, all_links))
            if new_href:
                print('url match !!  : ', new_href, '\n')
                # Copy this link to (indeed) url section
                current_url = driver.current_url
                print('Current url running :  ', current_url, '\n')

                # will use this variable in another place
                global_pattern = r'https://\w+\.\w+\.com/'
                slice_current_url = re.search(
                    global_pattern, current_url)  # /\w+\?\w*\=\w+&\w*\=
                # group() will omit -->  <re.Match object; span=(0, 21)
                if slice_current_url:
                    clean_url = slice_current_url.group()
                # new_url = list(filter(slice_current_url.search, current_url))

                # this will take form index(22)='emploi' until the end
                print('current url after slicing is  : ', clean_url)
                for i in new_href:
                    slice_new_href = i[22::]
                    print('new href after slicing : ',
                          slice_new_href, '\n')

                # Combine the Two nw urls
                final_url = clean_url + slice_new_href
                if final_url:
                    time.sleep(3)
                    driver.get(final_url)
                    time.sleep(6)
                    # Dissmiss The popup window if showed
                    action = ActionChains(driver)
                    popup_foreground = driver.find_element_by_xpath(
                        '//*[@id="popover-foreground"]')
                    action.move_to_element(popup_foreground).perform()
                    popup_dismiss = driver.find_element_by_xpath(
                        '//*[@id="popover-close-link"]')
                    action.move_to_element(popup_dismiss).perform()
                    popup_dismiss.click()

                    # Sorting by available Contract types
                    # Check first if sorting by job contract exists or not
                    top_level_tag = driver.find_element_by_id(
                        "JOB_TYPE_rbo")
                    if top_level_tag:
                        contract_types = []
                        contracts_href = []
                        try:
                            next_ul = top_level_tag.find_element_by_tag_name(
                                'ul')
                            for i in next_ul.find_elements_by_tag_name('li'):
                                link = i.find_element_by_tag_name('a')
                                # For getting all hrefs
                                get_titles = link.get_attribute('title')
                                get_hrefs = link.get_attribute('href')
                                contract_types.append(get_titles)
                                contracts_href.append(get_hrefs)
                            print('Found types : ', contract_types, '\n')

                            # Will be deleted later
                            print(' COntracts Urls : ',
                                  contracts_href, '\n')
                            my_type = input(
                                str('Enter Contract sorting type : '))

                            # Making dic to hundle frensh language cases
                            dic = {
                                'CDI': 'permanent', 'Intréim': 'temporary', 'Temp plein': 'full time',
                                'Stage': 'internship', 'Freelance / Ind�pendant': 'subcontract', 'CDD': 'contract',
                                'Temp partiel': 'parttime', 'Apprentissage / Alternance': 'apprenticeship'
                            }
                            # match user input against dic.values to get the url
                            for key, value in dic.items():
                                try:
                                    if key == my_type:
                                        print('match is : ', value)
                                        # Get matched link and
                                        find_url = re.compile('jt=' + value)
                                        found = list(
                                            filter(find_url.search, contracts_href))
                                        print('url match is : ', found)
                                        # Next to slice url match   (emploi..)
                                        # must be done with regex later
                                        for i in found:
                                            mid_url = i[22::]
                                            print('mid url is : ', mid_url)
                                            if mid_url:
                                                use_this = clean_url + mid_url
                                                driver.get(use_this)
                                                time.sleep(5)
                                except:
                                    print('exception')
                        except:
                            Exception()
                    else:
                        print('No Contract Types Available')
                else:
                    print('Invalid Url')
            else:
                print('Nothing Match Your title in hrefs list  !!')
    else:
        print('somthing here')
        # logic if dropdown filter wwas giving

        # # In case we have dropdown filtering
        # drop_location = []
        # span_id = driver.find_element_by_id('filter-location')
        # dropdown_ul = span_id.find_element_by_tag_name('ul')
        # for my_lists in dropdown_ul.find_elements_by_tag_name('li'):
        #     scrapp = my_lists.find_element_by_tag_name('a')
        #     data = scrapp.get_attribute('title')
        #     drop_location.append(data)
        # print('Search found : ', drop_location)


def save_jobs():
    # i set this to loop through 7 pages max // will handle the pages later
    #pages_to_loop_through = 7
    page = 1
    word = 'Suivant&nbsp'  # = Next  #pagination is not working yet
    try:
        print(' page number is ', page)
        job_titles = []
        job_link = []
        results_col = driver.find_element_by_xpath('//*[@id="resultsCol"]')
        all_rs = results_col.find_elements_by_class_name(
            'jobsearch-SerpJobCard')
        # loop throug all these results
        for i in all_rs:
            title_name = i.find_element_by_tag_name('div')
            title = title_name.find_element_by_tag_name(
                'a').text
            job_titles.append(title)
            title_link = title.get_attribute('href')
            job_link.append(title_link)
        print(' job name  :  {} , it\'s url : {}').format(
            job_titles,)

        # html = driver.find_element_by_tag_name('html')
        # html.send_keys(Keys.END)
        # pagination = results_col.find_element_by_xpath(
        #     '//div[25]/a[3]/span/span').text
        # print("text is ", pagination)
        # if word in pagination:
        #     next_link = results_col.find_element_by_xpath(
        #         '//div[25]/a[3]').get_attribute('href')
        #     print('next link will be  :',  next_link)
        #     next_link.click()
        #     page = page + 1
        # else:
        #     print('no other pages available; all job titles has been scrapped')

    except:
        Exception()

    # Saving the data into a json file


# Functions call
enter_clear_location()
sort_by()
save_jobs()
