import scrapy

class BloomSpider(scrapy.Spider):

    name = "bloom"

    start_urls = [
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=200',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=199',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=198',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=197',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=196',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=195',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=194',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=193',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=192',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=191',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=190',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=189',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=188',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=187',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=186',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=185',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=184',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=183',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=182',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=181',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=180',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=179',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=178',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=177',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=176',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=175',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=174',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=173',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=172',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=171',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=170',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=169',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=168',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=167',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=166',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=165',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=164',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=163',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=162',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=161',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=160',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=159',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=158',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=157',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=156',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=155',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=154',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=153',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=152',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=151',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=150',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=149',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=148',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=147',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=146',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=145',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=144',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=143',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=142',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=141',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=140',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=139',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=138',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=137',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=136',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=135',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=134',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=133',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=132',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=131',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=130',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=129',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=128',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=127',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=126',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=125',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=124',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=123',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=122',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=121',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=120',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=119',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=118',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=117',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=116',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=115',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=114',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=113',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=112',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=111',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=110',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=109',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=108',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=107',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=106',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=105',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=104',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=103',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=102',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=101',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=100',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=99',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=98',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=97',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=96',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=95',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=94',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=93',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=92',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=91',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=90',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=89',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=88',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=87',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=86',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=85',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=84',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=83',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=82',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=81',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=80',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=79',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=78',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=77',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=76',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=75',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=74',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=73',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=72',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=71',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=70',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=69',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=68',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=67',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=66',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=65',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=64',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=63',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=62',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=61',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=60',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=59',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=58',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=57',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=56',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=55',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=54',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=53',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=52',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=51',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=50',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=49',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=48',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=47',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=46',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=45',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=44',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=43',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=42',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=41',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=40',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=39',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=38',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=37',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=36',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=35',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=34',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=33',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=32',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=31',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=30',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=29',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=28',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=27',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=26',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=25',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=24',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=23',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=22',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=21',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=20',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=19',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=18',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=17',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=16',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=15',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=14',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=13',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=12',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=11',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=10',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=9',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=8',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=7',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=6',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=5',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=4',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=3',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=2',
        'https://www.lesechos.fr/finance-marches/marches-financiers/marches-boursiers?page=1'
    ]

    def parse(self, response):
        for bloom in response.xpath("//div[@class='sc-13mnsd1-2 bpFEdF']"):
            yield {
                'headline': bloom.xpath(".//h3/text()").extract(),
                'description':bloom.xpath(".//div[@class='a3uhlr-0 lkYJVA']/text()").extract(),
                'date': bloom.xpath(".//div/span/text()").extract()
            }

        # for bloom in response.xpath("//ul[@class='sc-14kwckt-18 tez3o0-1 gNfAhj']"):
        #     yield {
        #         'theme': bloom.xpath("//li/a/text()").extract()
        #     }
