from robocorp.tasks import task
from robocorp import browser


onboardingurl = "https://user.staging-vapaus.com/onboarding" #URL is not yet dynamic, the url link will be extracted from the email in the future
country = "Finland" #country is not yet dynamic
firstname = "Karla" #firstname is not yet dynamic
lastname = "VCTester" #lastname is not yet dynamic
phonenumber = "+358401234567" #phonenumber is not yet dynamic
streetaddress = "Vapaus street 1" #streetaddress is not yet dynamic
postalcode = "00100" #postalcode is not yet dynamic
city = "Helsinki" #city is not yet dynamic
employer = "Karla Newbies Oy" #employer is not yet dynamic
benefit = "Karla Newbies Oy (PRO)" #benefit is not yet dynamic
employeeNumber = "666" #employeeNumber is not yet dynamic
costCenter = "IT" #costCenter is not yet dynamic

@task
def onboarding():
    """
    Navigates to onboarding page from given url.
    Completes onboarding with given variables.
    Takes a screenshot of the completed onboarding page. 
    """
    browser.configure(
        slowmo=100, 
    )
    open_the_onboarding_website()
    complete_onboarding_select_country()
    complete_onboarding_complete_your_profile()
    confirm_your_employer()
    choose_a_bike_benefit()
    fill_in_employment_details_if_appears()
    accept_benefit_guidelines()
    take_screenshot_of_completed_onboarding()

    
def open_the_onboarding_website():
    """Navigates to the given URL"""
    browser.goto(onboardingurl)

def complete_onboarding_select_country():
    """Completes the onboarding wizards first page - select country"""
    page = browser.page()
    page.click("button.sc-dAlyuH.euKOxu") # Click "Get Started" button
    page.click("button.sc-guJBdh.kxzKMG.MuiSelect-root") # Click country selector to open dropdown
    page.wait_for_selector("ul[role='listbox']")
    page.click(f"ul[role='listbox'] >> li[role='option'] >> text={country}") # Select the country option from the listbox
    page.click("button.sc-dAlyuH.jlFkMd") # Click "Next" button on the "Select your country" screen

def complete_onboarding_complete_your_profile():
    """Fills in the user details in the onboarding form"""
    page = browser.page()
    page.fill("input[name='firstName']", firstname)
    page.fill("input[name='lastName']", lastname)
    page.fill("input[name='phoneNumber']", phonenumber)
    page.fill("input[name='address']", streetaddress)
    page.fill("input[name='postCode']", postalcode)
    page.fill("input[name='city']", city)
    page.click("button.sc-dAlyuH.jlFkMd") # Click "Next" button on the "Complete your profile" screen

def confirm_your_employer():
    """Confirms the employer"""
    page = browser.page()
    page.click("button.sc-guJBdh.kxzKMG.MuiSelect-root") # Click Employer selector to open dropdown
    page.wait_for_selector("ul[role='listbox']")
    page.click(f"ul[role='listbox'] >> li[role='option'] >> text={employer}") # Select the employer option from the listbox
    page.click("button.sc-dAlyuH.jlFkMd") # Click "Next" button on the "Confirm your employer" screen


def choose_a_bike_benefit():
    """Chooses a bike benefit"""
    page = browser.page()
    page.click("button.sc-guJBdh.kxzKMG.MuiSelect-root") # Click Benefit selector to open dropdown
    page.wait_for_selector("ul[role='listbox']")
    page.click(f"ul[role='listbox'] >> li[role='option'] >> text={benefit}") # Select the benefit option from the listbox
    page.click("button.sc-dAlyuH.jlFkMd") # Click "Next" button on the "Choose a bike benefit" screen
    
def fill_in_employment_details_if_appears():
    """Fills in employment details if the employment details screen appears"""
    page = browser.page()
    page.wait_for_timeout(1000)  # Wait 1 second to ensure the page is fully rendered

    filled = False

    if page.locator("input[name='employeeNumber']").is_visible():
        page.fill("input[name='employeeNumber']", employeeNumber)
        filled = True
    if page.locator("input[name='costCenter']").is_visible():
        page.fill("input[name='costCenter']", costCenter)
        filled = True

    if filled:
        page.click("button.sc-dAlyuH.jlFkMd")  # Click "Next" only if a field was filled

def accept_benefit_guidelines():
    """Accepts the benefit guidelines"""
    page = browser.page()
    page.click("button.sc-dAlyuH.euKOxu") # Click "Next" button on the "Benefit guidelines" screen
    
    page.wait_for_selector("h1.sc-gEvEer.ewqLKH") # Wait for the "Nice, all done!" screen to appear
    page.click("button.sc-dAlyuH.euKOxu") # Click "Continue" button on the final confirmation screen
    
def take_screenshot_of_completed_onboarding():
    """Takes a screenshot of the completed onboarding page"""
    page = browser.page()
    page.wait_for_selector("h1.sc-gEvEer.ewqLKH") # Wait for the "Ready to get a bike?" screen to appear
    page.wait_for_timeout(1000)  # Wait 1 second to ensure the page is fully rendered
    
    screenshot_path = f"output/screenshots/onboarding_confirmations/{firstname+lastname}_onboarding_completed.png"
    page.screenshot(path=screenshot_path)