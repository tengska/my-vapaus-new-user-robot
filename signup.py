from robocorp.tasks import task
from robocorp import browser


url = "https://user.staging-vapaus.com/" #URL is not yet dynamic
language = "EN" #language is not yet dynamic
email = "karla+vc8@vapaus.io" #email is not yet dynamic
pwd = email #password is the same as email for testing purposes


@task
def robot_vapaus_new_user_account():
    """
    Navigates to sign up page from given url and selects the user language.
    Fills the form for a new user account with given email and password.
    Accepts terms and conditions and submits the registration form.
    Takes a screenshot of the registration confirmation page. 
    """
    browser.configure(
        slowmo=100,
    )
    open_the_vapaus_website()
    navigate_to_sign_up_page()
    select_language()
    fill_in_user_details()
    accept_terms_and_conditions()
    submit_registration_form()

def open_the_vapaus_website():
    """Navigates to the given URL"""
    browser.goto(url)

def navigate_to_sign_up_page():
    """Navigates to the sign-up page from URL"""
    page = browser.page()
    page.click("a.sc-hknOHE.kCOwFU")

def select_language():
    """Selects the language from the language selector for the user"""
    page = browser.page()
    page.click("button.sc-fBWQRz.vgfjf.MuiSelect-root")
    page.wait_for_selector("ul[role='listbox']")
    page.click(f"ul[role='listbox'] >> li[role='option'] >> text={language}") # Select the "EN" option from the listbox

def fill_in_user_details():
    """Fills in the user details in the sign-up form"""
    page = browser.page()
    page.fill("input[name='email']", email)
    page.fill("input[name='password']", pwd)

def accept_terms_and_conditions():
    """Accepts the terms and conditions"""
    page = browser.page()
    page.click("label.sc-dAbbOL.eqZbjJ")

def submit_registration_form():
    """Submits the registration form and takes a screenshot of the confirmation page"""
    page = browser.page()
    page.click("button.sc-dAlyuH.jlFkMd")
    page.wait_for_url("**/email-not-verified")
    page.wait_for_selector("h1.sc-gEvEer.hzdMCQ")
    page.wait_for_timeout(1000)  # Wait 1 second to ensure the page is fully rendered

    email_prefix = email.split("@")[0]
    screenshot_path = f"output/screenshots/{email_prefix}_registration_confirmation.png"
    page.screenshot(path=screenshot_path)

# If email is not received, click send again button.sc-hknOHE.kCOwFU
    # page.click("button.sc-hknOHE.kCOwFU")

# def navigate_back_to_sign_up_page():
#    """Navigates back to the sign-up page"""
#    page = browser.page()
#    page.click("button.sc-hknOHE.gUxZgI")  # Click the back button