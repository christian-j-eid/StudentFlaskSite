from flask import Flask, render_template, request, redirect, session, url_for
import json
import requests



app = Flask(__name__)

kai_users = 'data/kai_users.json'
noah_users = 'data/noah_users.json'


@app.route('/')
@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/day', methods = ['GET', 'POST'])
def day():
    d = request.args["buttonId"]

    return render_template('day.html', day = d)

##RUSSELL
api_url = 'https://api.api-onepiece.com/v2/characters/en'


@app.route('/russell')
def russell():
    return render_template('russell_base.html')

@app.route('/russell_info')
def russel_info():
    response = requests.get(api_url)

    text = response.json()


    return render_template('russell_list_info.html', characters = text)

##LUKA

global nextcount
nextcount = 0


@app.route('/luka')
def luka():
    return render_template('luka_base.html')

@app.route('/LukaPokeDatabase')
def luka_database():
    URL = 'https://pokeapi.co/api/v2/pokemon/'

    res = requests.get(URL)
    data = res.json()
    current_data = data['results']
    info = {}
    count = 1
    return render_template('luka_main_database.html', data = current_data, c = 0)

@app.route('/lukaNext')
def next():
    global nextcount
    nextcount += 1
    next_URL = f'https://pokeapi.co/api/v2/pokemon/?offset={nextcount *20}&limit=20'
    res = requests.get(next_URL)
    data = res.json()
    current_data = data['results']
    return render_template('luka_main_database.html', data=current_data,c = nextcount)

@app.route('/lukaBack')
def back():
    global nextcount
    nextcount -= 1
    if nextcount == 0:
        return render_template('/luka')
    next_URL = f'https://pokeapi.co/api/v2/pokemon/?offset={nextcount *20}&limit=20'
    res = requests.get(next_URL)
    data = res.json()
    current_data = data['results']
    return render_template('luka_main_database.html', data=current_data,c = nextcount)

@app.route('/lukaMore', methods = ['POST'])
def more():
    if request.method == 'POST':
        if request.method == 'POST':
            data = request.form
            new_url = data['name']
            res = requests.get(new_url)
            data = res.json()
            # line underneath contains abilities, height, etc,
            data = data
            #We can also grab name
            pokemon = data['name']
            # WE specify abilities here
            # data = data['abilit']
    return render_template('luka_more.html', data=data, pokemon = pokemon)

##SAMPLE ROUTES
@app.route('/Sample')
def SampleStudentWebpage():
    return render_template('sample_base.html')


@app.route('/SamplePokeData')
def pokedata():
    url = 'https://pokeapi.co/api/v2/pokemon/'
    res = requests.get(url)
    data = res.json()

    return render_template('sample_poke.html', data = data['results'])


##BEN
@app.route('/ben')
def home():
    return render_template('ben_base.html')

@app.route('/benclick')
def click():
    return render_template('ben_beauty.html')

##
@app.route('/rose')
def rose_index():
    return render_template('index.html')

@app.route('/rose_mainpage')
def rose_mainpage():
    return render_template('mainpage.html')

@app.route('/rose_help')
def rose():
    return render_template('rose_help.html')

##KAI
@app.route('/kai')
def kai_homePage():
    return render_template('kai_base.html')


@app.route('/login')
def kai_login():
    return render_template('kai_login.html')

@app.route('/SignUp')
def kai_SignUp():
    return render_template('kai_SignUp.html')

@app.route('/LogOn')
def kai_LogOn():
    return render_template('kai_LogOn.html')

@app.route('/welcome', methods = ['POST'])
def kai_welcome():

    if request.method == 'POST':
        data = request.form
        username = data['uname']
        password = data['pass']

        userInfo = {"user":username,
                    'password':password,
                    'score': [0,0]
                    }
        with open(kai_users) as read_file:
            currentUsers = json.load(read_file)
        for eachUsers in currentUsers:
            if eachUsers['user'] == username:
                return render_template('kai_SignUp.html', taken = 'Username is taken')

        currentUsers.append(userInfo)
        with open(kai_users, 'w') as f:
            json.dump(currentUsers, f, indent= 2)
    return render_template('kai_welcome.html', user = username)

@app.route('/getAccount', methods = ['POST'])
def kai_validateLogin():
    if request.method == 'POST':
        data = request.form

        username = data['uname']
        password = data['pass']

        with open(kai_users) as read_file:
            currentUsers = json.load(read_file)
        usernames = []
        passwords = []
        for eachUser in currentUsers:
            usernames.append(eachUser['user'])

        # for eachPassword in currentUsers:
        #         usernames.append(eachPassword['password'])

        if username not in usernames:
            return render_template('kai_LogOn.html', err = "Error: \n Incorrect Username or Password")

        current = ''
        for each in currentUsers:
            if username == each['user']:
                current = username
                if each['password'] != password:
                    return render_template('kai_LogOn.html', err="Error: \n Incorrect Username or Password")
                if each['password'] == password:
                    user_url = f"/snake?user={current}"
                    return redirect(user_url)

@app.route('/snake')
def game():
    user = request.args["user"]
    return render_template('kai_game.html', user=user)


@app.route('/kai_submit', methods = ['POST'])
def k_submit():
    if request.method == 'POST':
        data = request.form
        user = data['user']
        score = data['score']



        t = f"Good job {user}! <br>  Your score of {score} will be submitted to the leaderboard."
    with open(kai_users) as read_file:
        currentUsers = json.load(read_file)
    current = ''
    # for each in currentUsers:
    #     if username == each['user']:
    #         current = username

    # currentUsers['current']['info']


    #
    #         eachUsers.append('')



    return render_template('kai_congrats.html', user = t)



@app.route('/kai_leaderboard')
def kai_leaderboard():
    data = 0
    return render_template('kai_leaderboard.html', data = data)


##NOAH
@app.route('/noah')
def noah_homePage():
    return render_template('noah.html')

@app.route('/noah_passwords')
def noah_PasswordsPage():
    return render_template('noah_userPasswords.html')

@app.route('/noah_links')
def naoh_login():
    return render_template('noah_importantLinks.html')

@app.route('/noah_signup')
def noah_signup():
    return render_template('noah_signup.html')

@app.route('/noah_welcome', methods = ['POST'])
def noah_welcome():

    if request.method == 'POST':
        data = request.form

        username = data['username']
        password = data['password']
        userInfo = {username:{
            'username':username,
            'password': password,
            'links':[],
            'passwords':[],
            'info':{}

        }}
        with open(noah_users) as read_file:
            currentUsers = json.load(read_file)
        usernames = []
        for each in currentUsers:
            usernames.append(list(each.keys()))

        username_strings = []
        for each in usernames:
            username_strings.append(each[0])
        if username in username_strings:
            return render_template('noah_signup.html', taken='Username is taken\nPlease try again')





        currentUsers.append(userInfo)
        with open(noah_users, 'w') as f:
            json.dump(currentUsers,f, indent= 2)


    return render_template('noah_welcome.html', user = username)

@app.route('/noah_getAccount', methods = ['POST'])
def noah_validateLogin():
    if request.method == 'POST':
        data = request.form

        username = data['username']
        password = data['password']

    with open(noah_users) as read_file:
        currentUsers = json.load(read_file)

    ##Getting all the usernames into a list with new format
    usernames = []
    for each in currentUsers:
        usernames.append(list(each.keys()))

    username_strings = []
    for each in usernames:
        username_strings.append(each[0])

    ## username_strings has all of the usernames in a list as strings!

    if username not in username_strings:
        return render_template('noah.html', err = 'This account does not exist')


    current = ''
    for name in username_strings:
        if name == username:
            current = name

    for each in currentUsers:
        if current in each:
            info = each[current]
            if info['password'] != password:
                return render_template('noah.html', err = 'Incorrect username or password')

            elif info['password'] == password:
                return render_template('noah_importantLinks.html', user=each[current]['username'], verified = password, links = info['links'])


        #     return render_template('noah.html', err='Incorrect Username or Password')
        # else:
        #     return render_template('noah_importantLinks.html', user = current)




@app.route('/noah_addLink', methods = ['POST'])
def noah_addUserLink():
    if request.method == 'POST':
        data = request.form
        user = data['user']
        link = data['link']
        nickname = data['nickname']
        verified = data['verified']
    with open(noah_users) as read_file:
        currentUsers = json.load(read_file)

    #Getting all the usernames into a list with new format (repeating the signup)

    usernames = []
    for each in currentUsers:
        usernames.append(list(each.keys()))

    username_strings = []
    for each in usernames:
        username_strings.append(each[0])

    ## username_strings has all of the usernames in a list as strings!


    current = ''
    for name in username_strings:
        if name == user:
            current = name
    #Ensuring they got access with password! (Try)
    for each in currentUsers:
        if current in each:
            info = each[current]
            # if info['password'] != verified:
            #     return render_template('noah.html', err='You do not have Verified Access without Password!') got a lil buggy

    #Creating the link info!

    newInfo = {
        'link':link,
        'name':nickname
    }
    # copy = info
    # copy['links'].append(newInfo)
    userDict = {}
    for each in currentUsers:
        if current in each:
            each[current]['links'].append(newInfo)
            info = each
    # info['links'].append(newInfo)
    # info = {}
    # info[current] = info
    # info = info[current]

    # return render_template('noah_importantLinks.html', user=info , verified= verified, links=info)

    # info[current] = info['links'].append(newInfo)

    # return render_template('noah.html', err=info)
    # for i in range(len(currentUsers)):
    #     if current in currentUsers[i]:
    #         currentUsers[i] = info


    with open(noah_users, 'w') as f:
        json.dump(currentUsers, f, indent=2)


    return render_template('/noah_success.html', l = link, n = nickname, user = current, verified = verified)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=False, host = '0.0.0.0')
# if __name__ == '__main__':
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=8080)
