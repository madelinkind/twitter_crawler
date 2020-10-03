from crawler.io import load_users_list_from_file
import crawler.config as crawl_conf

success, users_list = load_users_list_from_file(crawl_conf.USERS_LIST)
if not success:
    print("Failed to load users list")

print(users_list)

print(crawl_conf.ACCESS_TOKEN)
print(crawl_conf.ACCESS_TOKEN_SECRET)
print(crawl_conf.CONSUMER_KEY)
print(crawl_conf.CONSUMER_KEY_SECRET)
print(crawl_conf.USERS_LIST)