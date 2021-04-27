import random

import keyboard
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from accounts.forms import AddAccount, AddComment
from accounts.models import Account, Comments, Profile
import time
from selenium import webdriver
from time import sleep
from django.contrib.auth.decorators import login_required
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# from selenium.common.exceptions import NoSuchElementException
@login_required(login_url='/accounts/login')
def createAccount(request):
    form = AddAccount()
    if request.method == 'POST':
        form = AddAccount(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:accountview')

    context = {'form': form}
    return render(request, 'accounts/addaccount.html', context)


@login_required(login_url='/accounts/login')
def updateaccount(request, id):
    acc = Account.objects.get(id=id)
    form = AddAccount(instance=acc)
    print(id)
    if request.method == 'POST':
        form = AddAccount(request.POST, instance=acc)
        if form.is_valid():
            form.save()
            return redirect('accounts:accountview')

    context = {'form': form}
    return render(request, 'accounts/updateaccount.html', context)


@login_required(login_url='/accounts/login')
def accountview(request):
    acc = Account.objects.all()
    return render(request, 'accounts/accountsview.html', {'acc': acc})


@login_required(login_url='/accounts/login')
def deleteaccount(request, id):
    obj = get_object_or_404(Account, id=id)
    obj.delete()
    return accountview(request)


@login_required(login_url='/accounts/login')
def home(request):
    accounts = Account.objects.filter(status=1)
    maximum = len(accounts)
    return render(request, 'accounts/index.html', { 'maximum': maximum})


@login_required(login_url='/accounts/login')
def addcomment(request):
    form = AddComment()
    if request.method == 'POST':
        form = AddComment(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:commentview')

    context = {'form': form}
    return render(request, 'accounts/addcomment.html', context)


@login_required(login_url='/accounts/login')
def updatecomment(request, id):
    acc = Comments.objects.get(id=id)
    form = AddComment(instance=acc)
    print(id)
    if request.method == 'POST':
        form = AddComment(request.POST, instance=acc)
        if form.is_valid():
            form.save()
            return redirect('accounts:commentview')

    context = {'form': form}
    return render(request, 'accounts/updatecomment.html', context)


@login_required(login_url='/accounts/login')
def commentview(request):
    comment = Comments.objects.all()
    return render(request, 'accounts/commentview.html', {'comment': comment})


@login_required(login_url='/accounts/login')
def deletecomment(request, id):
    obj = get_object_or_404(Comments, id=id)
    obj.delete()
    return commentview(request)


def logout_views(request):
    if request.method == 'POST':
        print("-------------")
        logout(request)
        return render(request, 'accounts/newlogin.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)

            # if 'next' in request.POST:
            #     return redirect(request.POST.get('next'))
            return redirect('accounts:abc')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/newlogin.html', {'form': form})


def reportview(request):
    return render(request, 'accounts/report.html')

def errormessage(request):
    return render(request,'accounts/error_message.html')


@login_required(login_url='/accounts/login')
def instabotcode(request):

    if request.method == 'POST':
        try:
            like = request.POST.get('liked')
            comment = request.POST.get('commented')
            story = request.POST.get('storyview')
            follow = request.POST.get('followed')
            accounts_no = request.POST.get('account_number_tag')
            like_report = 0
            comment_report = 0
            story_report = 0
            follow_report = 0
            acc_search = []
            acc_username = []
            acc_password = []
            comment_list = []
            comment = Comments.objects.all()
            accounts = Account.objects.filter(status=1)

            maximum = len(accounts)
            print(maximum)
            for com in comment:
                comment_list.append(com.title)
            # accounts.get(use)
            for acc in accounts:
                acc_username.append(acc.userid)
                acc_password.append(acc.password)

            print("-----------------")
            print(acc_username)
            print(acc_password)
            print("-----------------")
            print(random.choice(comment_list))
            if request.POST:
                target = request.POST.get('example-tags')
                acc_search = target.split(',')
                print(acc_search)
                for i in range(len(acc_search)):
                    print(acc_search[i])
                like = request.POST.get('liked')
                comment = request.POST.get('commented')
                story = request.POST.get('storyview')
                follow = request.POST.get('followed')
                pro = Profile(follow=follow, comment=comment, like=like, story=story)
                print(like)
                print(comment)
                print(story)
                print(follow)
                # pro.save()
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
            options = webdriver.ChromeOptions()
            options.headless = True
            options.add_argument(f'user-agent={user_agent}')
            options.add_argument("--window-size=1920,1080")
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--allow-running-insecure-content')
            options.add_argument("--disable-extensions")
            options.add_argument("--proxy-server='direct://'")
            options.add_argument("--proxy-bypass-list=*")
            options.add_argument("--start-maximized")
            options.add_argument('--disable-gpu')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--no-sandbox')
            driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)

            # chromepath = "chromedriver.exe"
            # driver = webdriver.Chrome(executable_path=chromepath)

            driver.get("chrome://settings/clearBrowserData")
            sleep(6)

            actions = ActionChains(driver)
            actions.send_keys(Keys.TAB * 7 + Keys.ENTER)
            actions.perform()
            keyboard.send("Enter")
            print('Cache Clear Successfully')
            driver.quit()


            # clearButton = driver.execute_script(
            #     "return document.querySelector('settings-ui').shadowRoot.querySelector('settings-main').shadowRoot.querySelector('settings-basic-page').shadowRoot.querySelector('settings-section > settings-privacy-page').shadowRoot.querySelector('settings-clear-browsing-data-dialog').shadowRoot.querySelector('#clearBrowsingDataDialog').querySelector('#clearBrowsingDataConfirm')")
            # # click on the clear button now
            # clearButton.click()


            # driver.findElement(By.name("s")).sendKeys(Keys.F5);

            # print(driver.title)
            # time.sleep(5)

            for login in range(int(accounts_no)):
                sleep(6)
                user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
                options = webdriver.ChromeOptions()
                options.headless = True
                options.add_argument(f'user-agent={user_agent}')
                options.add_argument("--window-size=1920,1080")
                options.add_argument('--ignore-certificate-errors')
                options.add_argument('--allow-running-insecure-content')
                options.add_argument("--disable-extensions")
                options.add_argument("--proxy-server='direct://'")
                options.add_argument("--proxy-bypass-list=*")
                options.add_argument("--start-maximized")
                options.add_argument('--disable-gpu')
                options.add_argument('--disable-dev-shm-usage')
                options.add_argument('--no-sandbox')
                driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)

                # chromepath = "chromedriver.exe"  # Headless
                # driver = webdriver.Chrome(executable_path=chromepath)

                driver.get('https://www.instagram.com/')

                wait = WebDriverWait(driver, 10)

                sleep(5)
                print('Webpage :' + driver.title)
                print("Username :" + acc_username[login])
                print("Password : " + acc_password[login])
                Username = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                    (By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")))
                Username.send_keys(acc_username[login])
                sleep(1)
                Password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                    (By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")))
                Password.send_keys(acc_password[login])
                time.sleep(3)

                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type=submit]'))).click()
                time.sleep(5)

                # try:
                #
                #     notnow = WebDriverWait(driver, 10).until(
                #         EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Not Now")]'))).click()
                #     sleep(5)
                #     notti = WebDriverWait(driver, 10).until(
                #         EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Not Now")]'))).click()
                #     if notti.is_displayed():
                #         notti.click()
                #         sleep(5)
                #
                # except:
                #     print('Notification notnow in Not Appear')
                #     pass

                try:
                    wrongpass = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@aria-atomic="true"]')))
                    if wrongpass.is_displayed():
                        print("Sorry, your password was incorrect.")
                        driver.quit()
                        # driver.refresh()
                        continue
                except:
                    print('Login Successfully  with : ' + acc_username[login])
                    pass

                try:
                    verifyacc = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/div[1]/div/div[2]/button')))
                    if verifyacc.is_displayed():
                        print('Verify Email - Switch to next account Successfully  : ' + acc_username[login])
                        driver.quit()
                        # sleep(3)
                        # driver.get('https://www.instagram.com/')
                        continue
                except:
                    print('Login Successfully  with : ' + acc_username[login])
                    pass

                for search in range(len(acc_search)):
                    sleep(5)
                    print('Search Name : ' + acc_search[search])
                    Search = wait.until(EC.visibility_of_element_located(
                        (By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')))
                    Search.send_keys(acc_search[search])
                    sleep(10)
                    Profile_Open = wait.until(EC.element_to_be_clickable(
                        (By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div')))
                    Profile_Open.click()
                    sleep(10)
                    if follow == None:
                        pass
                    else:
                        try:
                            # Follow
                            Follow = wait.until(
                                EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Follow")]'))).click()
                            time.sleep(5)
                            print('Follow Successfully  :' + acc_search[search])
                            follow_report += 1

                        except:
                            print('Already Follow :' + acc_search[search])
                            pass

                    if story == None:
                        pass
                    else:
                        try:
                            # Story
                            Story = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_6q-tv'))).click()
                            time.sleep(5)
                            # Close-Story
                            StoryClose = wait.until(
                                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/div[3]/button'))).click()
                            sleep(5)
                            print('Story Seen Successfully : ' + acc_search[search])
                            story_report += 1

                        except:
                            print('No story view')
                            sleep(5)
                            pass

                    # if like == None or comment == None:
                    #     pass
                    # else:
                    sleep(3)
                    Pic = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_9AhH0'))).click()
                    sleep(3)
                    # # # like = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')
                    # # # like.click()
                    # # # sleep(3)
                    if like == None:
                        pass
                    else:
                        try:
                            sleep(5)
                            like_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Like"]'))).click()
                            sleep(5)
                            print('Pic Liked Successfully : ' + acc_search[search])
                            like_report += 1
                        except:
                            print('Already Liked Pic :' + acc_search[search])
                            pass

                    if comment == None:
                        pass
                    else:
                        try:
                            sleep(5)
                            Post = wait.until(
                                EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"OK")]'))).click()
                            print('Restricted Comment')

                        except:
                            comment = wait.until(EC.visibility_of_element_located(
                                (By.XPATH, '/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[2]/button')))
                            if comment.is_displayed():
                                comment.click()
                                sleep(3)
                            msg = wait.until(EC.element_to_be_clickable(
                                (By.XPATH,
                                 '/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea'))).send_keys(
                                random.choice(comment_list))
                            sleep(3)
                            Post = wait.until(
                                EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Post")]'))).click()
                            sleep(5)
                            print('Comment Successfully')
                            comment_report += 1
                            # print('Already Comment :' + acc_search[search])
                            pass
                            sleep(3)

                    # if like == None or comment == None:
                    #     pass
                    # else:
                    Pic_close = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Close"]'))).click()
                    sleep(2)

                LogOutBtn = wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img'))).click()
                time.sleep(3)
                Logout = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div'))).click()

                sleep(5)
                driver.quit()
                sleep(4)
                print('Logout Successfully ')
                print('--------')




            # driver.quit()

            return render(request, 'accounts/report.html',
                          {'target': target, 'like_report': like_report, 'comment_report': comment_report,
                           'story_report': story_report, 'follow_report': follow_report})
        except:
            # return HttpResponse("Network problem")
            return render(request, 'accounts/error_message.html')