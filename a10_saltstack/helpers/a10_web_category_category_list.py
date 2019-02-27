# Copyright 2019 A10 Networks
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



# Hacky way of having access to object properties for evaluation
AVAILABLE_PROPERTIES = [    "abortion",
    "adult_and_pornography",
    "alcohol_and_tobacco",
    "auctions",
    "bot_nets",
    "business_and_economy",
    "cdns",
    "cheating",
    "computer_and_internet_info",
    "computer_and_internet_security",
    "confirmed_spam_sources",
    "cult_and_occult",
    "dating",
    "dead_sites",
    "drugs",
    "dynamic_comment",
    "educational_institutions",
    "entertainment_and_arts",
    "fashion_and_beauty",
    "financial_services",
    "food_and_dining",
    "gambling",
    "games",
    "government",
    "gross",
    "hacking",
    "hate_and_racism",
    "health_and_medicine",
    "home_and_garden",
    "hunting_and_fishing",
    "illegal",
    "image_and_video_search",
    "internet_communications",
    "internet_portals",
    "job_search",
    "keyloggers_and_monitoring",
    "kids",
    "legal",
    "local_information",
    "malware_sites",
    "marijuana",
    "military",
    "motor_vehicles",
    "music",
    "a10_name",
    "news_and_media",
    "nudity",
    "online_greeting_cards",
    "open_http_proxies",
    "parked_domains",
    "pay_to_surf",
    "peer_to_peer",
    "personal_sites_and_blogs",
    "personal_storage",
    "philosophy_and_politics",
    "phishing_and_other_fraud",
    "private_ip_addresses",
    "proxy_avoid_and_anonymizers",
    "questionable",
    "real_estate",
    "recreation_and_hobbies",
    "reference_and_research",
    "religion",
    "sampling_enable",
    "search_engines",
    "sex_education",
    "shareware_and_freeware",
    "shopping",
    "social_network",
    "society",
    "spam_urls",
    "sports",
    "spyware_and_adware",
    "stock_advice_and_tools",
    "streaming_media",
    "swimsuits_and_intimate_apparel",
    "training_and_tools",
    "translation",
    "travel",
    "uncategorized",
    "unconfirmed_spam_sources",
    "user_tag",
    "uuid",
    "violence",
    "weapons",
    "web_advertisements",
    "web_based_email",
    "web_hosting_sites",
]

MODULE_NAME = "category-list"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/web-category/category-list/{name}"
    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/web-category/category-list/{name}"
    f_dict = {}
    f_dict["name"] = kwargs["a10-name"]

    return url_base.format(**f_dict)