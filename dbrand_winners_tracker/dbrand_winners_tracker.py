import requests
import bs4
import re

url = "https://dbrand.com/winners"
twitter = "@Iftakha39078519"
instagram = "@iftakharn19"
def did_i_win(winners_list,user_name):
    return bool(winners_list.get(user_name))


#getting the html response using requests library
response = requests.get(url)
soup = bs4.BeautifulSoup(response.content, features="html.parser")
a=soup.find_all('div', attrs={'class':"attr winner-name"})


twitter_winners = {}
instagram_winners = {}
next_winner_sellection = soup.find('p',attrs={"class":"countdown countdown--static"}).get_text(strip=True) #next winner selection date

for i in a:
    username = i.get_text(strip=True)
    user_profile_url = i.find_next('a').get('href')
    if username=="Username":
        continue
    if "twitter" in user_profile_url:
        twitter_winners[username] = user_profile_url
    elif "instagram" in user_profile_url:
        instagram_winners[username] = user_profile_url

print('\nTwitter winners are:')
for key in twitter_winners:
    print(key)

print('\nInstagram winners are:')
for key in instagram_winners:
    print(key)
print()

if did_i_win(twitter_winners,twitter):
    print('You won the giveaway on Twitter account!\nCongratulations!!!')
elif did_i_win(instagram_winners,instagram):
    print('You won the giveaway on Instagram account!\nCongratulations!!!')
else:
    print("You haven't win the giveaway yet better luck next time.")
    print(f"Next winner will be selected on {next_winner_sellection}.")

if input("Do you want to save the winners list?(y/n) ").lower()=="y":
    with open("winners.txt","w") as winners:
        winners.write("Instagram winners are:\n")
        for usr,link in instagram_winners.items():
            winners.write(f"{usr},{link}\n")
        winners.write("\n\nTwitter winners are:\n")
        for usr,link in twitter_winners.items():
            winners.write(f"{usr},{link}\n")