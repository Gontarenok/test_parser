# import requests
# from bs4 import BeautifulSoup
# import json
#
# def fetch(url, params):
#     headers = params["headers"]
#     body = params["body"]
#     method = params["method"]
#
#     if method == "POST":
#         return requests.post(url, headers=headers, data=body)
#
#     if method == "GET":
#         return requests.get(url, headers=headers)
#
# metro = fetch("https://api.metro-cc.ru/products-api/graph", {
#   "headers": {
#     "accept": "application/json, text/plain, */*",
#     "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
#     "content-type": "application/json",
#     "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-site",
#     "cookie": "spid=1687818476030_2c206ae74e31040a3cef8121093cb920_0s7ek70nfa8w50pe; _slid=649a10f20c95a157330d7f0d; _gcl_au=1.1.794558340.1687818490; metro_api_session=EbL1yWr94Oeb7LqS5NxE7lHoHzTSlJvxa37nX08n; tmr_lvid=f8dd3223b90d0173ebe0c20fc9e27314; tmr_lvidTS=1687818496533; _ym_uid=1687818497143300958; _ym_d=1687818497; _ym_isad=1; metro_user_id=a8b1a19a282cd496862c91157d9f5575; _gid=GA1.2.1672498404.1687818502; uxs_uid=c2b664d0-1470-11ee-98fb-cb8695bccd8f; fam_user=2 5; _slid_server=649a10f20c95a157330d7f0d; _slsession=23F10CB7-BDA1-442B-9503-59A6B4DD96FA; _slfreq=633ff97b9a3f3b9e90027740%3A633ffa4c90db8d5cf00d7810%3A1687834474; _ym_visorc=b; _ga=GA1.2.692445247.1687818502; mindboxDeviceUUID=e1a4fc6a-9b05-4bda-ab20-4909f15dc27b; directCrm-session=%7B%22deviceGuid%22%3A%22e1a4fc6a-9b05-4bda-ab20-4909f15dc27b%22%7D; _ga_VHKD93V3FV=GS1.1.1687827271.4.1.1687828398.0.0.0; spsc=1687828446066_30c89d15dbc1bf67482726972119deb8_a5476469b72f558bb72e6aae99c6a060",
#     "Referer": "https://online.metro-cc.ru/",
#     "Referrer-Policy": "no-referrer-when-downgrade"
#   },
#   "body": "{\"query\":\"\\n  query Query($storeId: Int!, $slug: String!, $attributes:[AttributeFilter], $filters: [FieldFilter], $from: Int!, $size: Int!, $sort: InCategorySort, $in_stock: Boolean, $eshop_order: Boolean, $is_action: Boolean, $price_levels: Boolean) {\\n    category (storeId: $storeId, slug: $slug, inStock: $in_stock, eshopAvailability: $eshop_order, isPromo: $is_action, priceLevels: $price_levels) {\\n      id\\n      name\\n      slug\\n      id\\n      parent_id\\n      meta {\\n        description\\n        h1\\n        title\\n        keywords\\n      }\\n      disclaimer\\n      description {\\n        top\\n        main\\n        bottom\\n      }\\n#      treeBranch {\\n#        id\\n#        name\\n#        slug\\n#        children {\\n#          category_type\\n#          id\\n#          name\\n#          slug\\n#          children {\\n#            category_type\\n#            id\\n#            name\\n#            slug\\n#            children {\\n#              category_type\\n#              id\\n#              name\\n#              slug\\n#              children {\\n#                category_type\\n#                id\\n#                name\\n#                slug\\n#              }\\n#            }\\n#          }\\n#        }\\n#      }\\n      breadcrumbs {\\n        category_type\\n        id\\n        name\\n        parent_id\\n        parent_slug\\n        slug\\n      }\\n      promo_banners {\\n        id\\n        image\\n        name\\n        category_ids\\n        virtual_ids\\n        type\\n        sort_order\\n        url\\n        is_target_blank\\n        analytics {\\n          name\\n          category\\n          brand\\n          type\\n          start_date\\n          end_date\\n        }\\n      }\\n\\n\\n      dynamic_categories(from: 0, size: 9999) {\\n        slug\\n        name\\n        id\\n      }\\n      filters {\\n        facets {\\n          key\\n          total\\n          filter {\\n            id\\n            name\\n            display_title\\n            is_list\\n            is_main\\n            text_filter\\n            is_range\\n            category_id\\n            category_name\\n            values {\\n              slug\\n              text\\n              total\\n            }\\n          }\\n        }\\n      }\\n      total\\n      prices {\\n        max\\n        min\\n      }\\n      pricesFiltered {\\n        max\\n        min\\n      }\\n      products(attributeFilters: $attributes, from: $from, size: $size, sort: $sort, fieldFilters: $filters)  {\\n        health_warning\\n        limited_sale_qty\\n        id\\n        slug\\n        name\\n        name_highlight\\n        article\\n        is_target\\n        category_id\\n        url\\n        images\\n        pick_up\\n        icons {\\n          id\\n          badge_bg_colors\\n          caption\\n          image\\n          type\\n          is_only_for_sales\\n          stores\\n          caption_settings {\\n            colors\\n            text\\n          }\\n          stores\\n          sort\\n          image_png\\n          image_svg\\n          description\\n          end_date\\n          start_date\\n          status\\n        }\\n        manufacturer {\\n          id\\n          image\\n          name\\n        }\\n        packing {\\n          size\\n          type\\n          pack_factors {\\n            instamart\\n          }\\n        }\\n        stocks {\\n          value\\n          text\\n          eshop_availability\\n          scale\\n          prices_per_unit {\\n            old_price\\n            offline {\\n              price\\n              old_price\\n              type\\n              offline_discount\\n              offline_promo\\n            }\\n            price\\n            is_promo\\n            levels {\\n              count\\n              price\\n            }\\n            discount\\n          }\\n          prices {\\n            price\\n            is_promo\\n            old_price\\n            offline {\\n              old_price\\n              price\\n              type\\n              offline_discount\\n              offline_promo\\n            }\\n            levels {\\n              count\\n              price\\n            }\\n            discount\\n          }\\n        }\\n      }\\n    }\\n  }\\n\",\"variables\":{\"isShouldFetchOnlyProducts\":true,\"slug\":\"chistyaschie-sredstva\",\"storeId\":10,\"sort\":\"priceAsc\",\"size\":30,\"from\":0,\"filters\":[],\"attributes\":[],\"in_stock\":true,\"eshop_order\":false}}",
#   "method": "POST"
# })
#
# print(metro)

# ошибка 403: Ресурс, к которому вы пытаетесь получить доступ, запрещен: у вас нет прав для его просмотра.

# url = "https://api.metro-cc.ru/products-api/graph"
# headers = {"content-type": "application/json",
#            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
# body = {"query": "query { __typename }"}
# response = requests.post(url, headers=headers, data=body)
#
# print(response)


