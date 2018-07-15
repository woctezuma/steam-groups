import json
import pathlib
import time

import requests


def get_data_folder():
    return 'data/'


def get_api_key_filename():
    return get_data_folder() + 'api_key.txt'


def get_member_list_filename():
    return get_data_folder() + 'members_list.txt'


def load_api_key():
    api_key_filename = get_api_key_filename()
    with open(api_key_filename, 'r') as f:
        data = f.readlines()
    api_key = data[0]
    return api_key


def load_member_list():
    member_list_filename = get_member_list_filename()
    with open(member_list_filename, 'r') as f:
        data = f.readlines()
    member_list = [int(steam_id.strip()) for steam_id in data]
    return member_list


def get_library_folder():
    data_path = get_data_folder() + 'library_with_f2p/'

    pathlib.Path(data_path).mkdir(parents=True, exist_ok=True)

    return data_path


def get_recently_played_folder():
    data_path = get_data_folder() + 'recently_played/'

    pathlib.Path(data_path).mkdir(parents=True, exist_ok=True)

    return data_path


def get_steam_api_library_url():
    return 'https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/'


def get_steam_api_recently_played_url():
    return 'https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v1/'


def download_user_data(steam_id, output_folder, steam_api_url, query_count=0):
    rate_limits = get_steam_api_rate_limits()

    library_filename = output_folder + str(steam_id) + '.json'

    try:
        with open(library_filename, 'r', encoding="utf8") as in_json_file:
            data_as_json = json.load(in_json_file)
        print('Loading data from cache for Steam-ID {}'.format(steam_id))
    except FileNotFoundError:

        if query_count >= rate_limits['max_num_queries']:
            cooldown_duration = rate_limits['cooldown']
            print('Number of queries {} reached. Cooldown: {} seconds'.format(query_count, cooldown_duration))
            time.sleep(cooldown_duration)
            query_count = 0

        print("Downloading and caching data for Steam-ID {}".format(steam_id))

        data_request = dict()
        data_request['key'] = load_api_key()
        data_request['steamid'] = steam_id
        data_request['include_played_free_games'] = 1

        response = requests.get(steam_api_url, params=data_request)
        data_as_json = response.json()

        query_count += 1

        with open(library_filename, 'w', encoding="utf8") as cache_json_file:
            # Enforce double-quotes instead of single-quotes. Reference: https://stackoverflow.com/a/8710579/
            data_as_str = json.dumps(data_as_json)
            print(data_as_str, file=cache_json_file)

    return data_as_json, query_count


def download_user_library(steam_id, query_count=0):
    output_folder = get_library_folder()
    steam_api_url = get_steam_api_library_url()

    library_data, query_count = download_user_data(steam_id, output_folder, steam_api_url, query_count)

    return library_data, query_count


def download_user_recently_played_games(steam_id, query_count=0):
    output_folder = get_recently_played_folder()
    steam_api_url = get_steam_api_recently_played_url()

    recently_played_data, query_count = download_user_data(steam_id, output_folder, steam_api_url, query_count)

    return recently_played_data, query_count


def get_steam_api_rate_limits():
    # Objective: return the rate limits of Steam API.

    rate_limits = {
        'max_num_queries': 150,
        'cooldown': (5 * 60) + 10,  # 5 minutes plus a cushion
    }

    return rate_limits


def batch_download():
    member_list = load_member_list()

    query_count = 0

    for steam_id in member_list:
        library_data, query_count = download_user_library(steam_id, query_count)

        # recently_played_data, query_count = download_user_recently_played_games(steam_id, query_count)

    return


def main():
    batch_download()

    return True


if __name__ == '__main__':
    main()
