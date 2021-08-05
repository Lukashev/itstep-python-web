from django.shortcuts import render
from datetime import datetime

teams = {
    'recipes': {
        'goulash': [
            'Мясо помыть, нарезать кубиками, посолить, поперчить, обжарить в растительном масле.',
            'Добавить мелко нашинкованный лук, посыпать мукой, обжарить. Шпаргалка Как нарезать репчатый лук',
            'Переложить в кастрюлю, залить 3 стаканами горячей воды, добавить томатную пасту, лавровый лист, накрыть крышкой и тушить 50 минут.'
        ],
        'dumplings': [
            'Підготуйте всі інгредієнти для приготування вареників із вишнею.',
            'Відміряйте 500 г борошна та пересипте в миску, додайте ½ ч. л. солі, 1 куряче яйце та 1 ст. л. соняшникової олії.',
            'Далі влийте 250 мл молока.'
        ]
    },
    'football': [
        'Roma FC',
        'Arsenal',
        'Chelsea'
    ],
    'basketball': [
        'Boston Celtics',
        'Atlanta Hawks',
        'Charlotte Hornets'
    ],
    'hockey': [
        'Boston Bruins',
        'Buffalo Sabres',
        'Florida Panthers'
    ]
}


def index(request):
    # get recipe by url param
    recipe = request.GET.get('recipe', None)
    action_list = None
    current_recipe = teams['recipes'].get(recipe)
    if recipe and current_recipe:
        action_list = teams['recipes'][recipe]
    section_list = teams.keys()
    # get greetings by day hour
    hour = datetime.now().hour
    if 4 <= hour < 12:
        greeting = 'Good morning!'
    elif 12 <= hour < 17:
        greeting = 'Good afternoon!'
    else:
        greeting = 'Good evening!'
    # render template and pass context variables
    return render(request, 'index.html', context={
        'section_list': list(section_list),
        'title': f'{greeting} Choose sport category...',
        'action_list': action_list or []
    })


def football(request):
    team_list = teams['football']
    return render(request, 'football.html', context={'team_list': team_list, 'title': 'Football Teams'})


def basketball(request):
    team_list = teams['basketball']
    return render(request, 'basketball.html', context={'team_list': team_list, 'title': 'Basketball Teams'})


def hockey(request):
    team_list = teams['hockey']
    return render(request, 'basketball.html', context={'team_list': team_list, 'title': 'Hockey Teams'})