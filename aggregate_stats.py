import json
import math

import steamspypi

from steam_groups import get_library_folder, load_member_list


def load_user_data(steam_id, data_folder, verbose=False):
    data_filename = data_folder + str(steam_id) + '.json'

    try:
        with open(data_filename, encoding="utf8") as in_json_file:
            data_as_json = json.load(in_json_file)

        if verbose:
            print(f'Loading data from cache for Steam-ID {steam_id}')

    except FileNotFoundError:
        data_as_json = {}

        if verbose:
            print(f'No data could be found for Steam-ID {steam_id}')

    return data_as_json


def batch_load_user_data(include_free_games=True, data_folder=None, verbose=False):
    if data_folder is None:
        data_folder = get_library_folder(include_free_games)

    data = {}

    for steam_id in load_member_list():
        user_data = load_user_data(steam_id, data_folder, verbose)

        if len(user_data) == 0:
            continue

        try:
            game_list = user_data['response']['games']
        except KeyError:
            if verbose:
                print(
                    f'Steam-ID {steam_id} does not share library information.',
                )
            game_list = []

        for game in game_list:
            app_id = game['appid']

            playtime_forever = game['playtime_forever']

            try:
                data[app_id]['num_players_forever'] += 1
                data[app_id]['playtime_forever'] += playtime_forever
            except KeyError:
                data[app_id] = {}
                data[app_id]['num_players_forever'] = 1
                data[app_id]['playtime_forever'] = playtime_forever

                data[app_id]['num_players_2weeks'] = 0
                data[app_id]['playtime_2weeks'] = 0

            try:
                playtime_2weeks = game['playtime_2weeks']
            except KeyError:
                continue

            data[app_id]['num_players_2weeks'] += 1
            data[app_id]['playtime_2weeks'] += playtime_2weeks

    return data


def compute_ranking(data, criterion=None):
    if criterion is None:
        criterion = 'num_players_forever'

    ranking = sorted(data.keys(), key=lambda x: data[x][criterion], reverse=True)

    return ranking


def print_ranking(ranking, data, criterion, max_ranking_length=100):
    steamspy_data = steamspypi.load()

    counter = 1

    width = 1 + math.floor(math.log10(max_ranking_length))

    if criterion == 'playtime_forever':
        title = 'The most played games ever'
    elif criterion == 'num_players_forever':
        title = 'The games with the highest number of owners'
    elif criterion == 'playtime_2weeks':
        title = 'The most played games during the first two weeks of July'
    else:
        if not (criterion == 'num_players_2weeks'):
            raise AssertionError()
        title = 'The games which were started by the highest number of people during the first two weeks of July'

    print(f'\n{title}\n')

    for app_id in ranking:
        if counter > max_ranking_length:
            break

        app_id_str = str(app_id)

        try:
            game_name = steamspy_data[app_id_str]['name']
            store_url = 'https://store.steampowered.com/app/'
        except KeyError:
            game_name = 'redacted'
            store_url = 'https://steamdb.info/app/'

        hyperlink = '[' + game_name + '](' + store_url + app_id_str + ')'

        criterion_value = data[app_id][criterion]

        print(f'{counter: >{width}}. {hyperlink} ({criterion}={criterion_value})')

        counter += 1

    return


def print_every_ranking(include_free_games=True, max_ranking_length=100):
    data = batch_load_user_data(include_free_games)

    criteria = [
        'playtime_forever',
        'num_players_forever',
        'playtime_2weeks',
        'num_players_2weeks',
    ]

    for criterion in criteria:
        ranking = compute_ranking(data, criterion)

        print_ranking(ranking, data, criterion, max_ranking_length)

    return


def main():
    include_free_games = True
    max_ranking_length = 1000
    print_every_ranking(include_free_games, max_ranking_length)

    return True


if __name__ == '__main__':
    main()
