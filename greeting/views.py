from django.shortcuts import render

# Create your views here.
def home(request):
	certification = [
		{
		'name': 'Modern PHP Web Development w/ MySQL, GitHub & Heroku',
		'link': 'https://ude.my/UC-789d1891-bffb-4979-a95d-9dcb0f9691a5/',
		'from': 'Udemy',
		'time': '7th Sept, 2021',
		},
		{
		'name': 'JavaScript Algorithms and Data Structures',
		'link': 'https://www.freecodecamp.org/certification/kylesinlynn/javascript-algorithms-and-data-structures',
		'from': 'freeCodeCamp',
		'time': '4th July, 2021',
		},
		{
		'name': 'Responsive Web Design',
		'link': 'https://freecodecamp.org/certification/kylesinlynn/responsive-web-design',
		'from': 'freeCodeCamp',
		'time': '7th June, 2021',
		},
		{
		'name': 'Python Core course',
		'link': 'https://www.sololearn.com/Certificate/1073-19030510/jpg/',
		'from': 'SoloLearn',
		'time': '3rd Aug, 2020',
		},
		{
		'name': 'C course',
		'link': 'https://www.sololearn.com/Certificate/1089-19030510/jpg/',
		'from': 'SoloLearn',
		'time': '15th May, 2021',
		},
	]
	languages = [
		{
			'name': 'Python3',
		},
	]
	frameworks = [
		{
			'name': 'Django',
		}
	]
	data = {
		'certification': certification,
		'languages': languages,
		'frameworks': frameworks,
	}
	return render(request, 'portfolio/home.html', data)

def projects_list(request):
	import requests, json
	url = "https://api.github.com/users/kylesinlynn/repos"
	response = requests.get(url)
	data = json.loads(response.text)
	repos = {'projects': data}
	return render(request, 'portfolio/projects_list.html', repos)

def contact(request):
	return render(request, 'portfolio/contact.html', {})