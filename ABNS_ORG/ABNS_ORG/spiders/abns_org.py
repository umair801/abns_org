import scrapy
from scrapy import FormRequest
from string import ascii_lowercase


class AbnsOrgSpider(scrapy.Spider):
    name = "abns_org"
    start_urls = ['https://abns.org/find_a_neurosurgeon/']

    def parse(self, response):
        for alphabet in ascii_lowercase:
            formdata = {
                'search-first-name': alphabet,
                'search-last-name': '',
                'search-cohort': '',
                'search-specialty': '',
                'search-country': '-----',
                'search-city': '',
                'search-zip': ''
            }
            yield FormRequest(
                url='https://abns.org/find_a_neurosurgeon/execute',
                formdata=formdata,
                callback=self.parse_data,
            )

    def parse_data(self, response):
        global abns_certificate
        rows = response.xpath('//div[@class="col-sm-3 mb-3 mb-sm-3"]')
        for row in rows:
            name = row.xpath('.//div[@class="card-header"]/strong/text()').get()

            abns_certificate1 = row.xpath(
                'normalize-space(.//*[contains(text(),"ABNS Certification")][1]/following-sibling::text())').getall()
            abns_certificate = abns_certificate1
            abns_certificate2 = row.xpath(
                'normalize-space(.//*[contains(text(),"ABNS Certification")][2]/following-sibling::text())').getall()
            abns_certificate3 = row.xpath(
                'normalize-space(.//*[contains(text(),"ABNS Certification")][3]/following-sibling::text())').getall()
            abns_certificate4 = row.xpath(
                'normalize-space(.//*[contains(text(),"ABNS Certification")][4]/following-sibling::text())').getall()
            abns_certificate5 = row.xpath(
                'normalize-space(.//*[contains(text(),"ABNS Certification")][5]/following-sibling::text())').getall()
            if len(abns_certificate2[0]) > 0:
                abns_certificate = f'{abns_certificate1}, {abns_certificate2}'
            if len(abns_certificate3[0]) > 0:
                abns_certificate = f'{abns_certificate1}, {abns_certificate2}, {abns_certificate3}'
            if len(abns_certificate4[0]) > 0:
                abns_certificate = f'{abns_certificate1}, {abns_certificate2}, {abns_certificate3}, {abns_certificate4}'
            if len(abns_certificate5[0]) > 0:
                abns_certificate = f'{abns_certificate1}, {abns_certificate2}, {abns_certificate3}, {abns_certificate4}, {abns_certificate5}'

            rfp_in_cns1 = row.xpath(
                'normalize-space(.//*[contains(text(),"RFP in CNS Endovascular Surgery")][1]/following-sibling::text())').getall()
            rfp_in_cns = rfp_in_cns1
            rfp_in_cns2 = row.xpath(
                'normalize-space(.//*[contains(text(),"RFP in CNS Endovascular Surgery")][2]/following-sibling::text())').getall()
            rfp_in_cns3 = row.xpath(
                'normalize-space(.//*[contains(text(),"RFP in CNS Endovascular Surgery")][3]/following-sibling::text())').getall()
            rfp_in_cns4 = row.xpath(
                'normalize-space(.//*[contains(text(),"RFP in CNS Endovascular Surgery")][4]/following-sibling::text())').getall()
            rfp_in_cns5 = row.xpath(
                'normalize-space(.//*[contains(text(),"RFP in CNS Endovascular Surgery")][5]/following-sibling::text())').getall()
            if len(rfp_in_cns2[0]) > 0:
                rfp_in_cns = f'{rfp_in_cns1}, {rfp_in_cns2}'
            if len(rfp_in_cns3[0]) > 0:
                rfp_in_cns = f'{rfp_in_cns1}, {rfp_in_cns2}, {rfp_in_cns3}'
            if len(rfp_in_cns4[0]) > 0:
                rfp_in_cns = f'{rfp_in_cns1}, {rfp_in_cns2}, {rfp_in_cns3}, {rfp_in_cns4}'
            if len(rfp_in_cns5[0]) > 0:
                rfp_in_cns = f'{rfp_in_cns1}, {rfp_in_cns2}, {rfp_in_cns3}, {rfp_in_cns4}, {rfp_in_cns5}'

            certified = row.xpath('.//*[contains(text(),"Certified:")]/text()[1]').get()
            if certified: certified = certified.strip().split(': ')[1]

            lifetime = row.xpath('.//*[contains(text(),"Lifetime:")]/text()[1]').get()
            if lifetime: lifetime = lifetime.strip().split(': ')[1]

            rfp_in_neuro1 = row.xpath(
                'normalize-space(.//*[contains(text(),"RFP in Neurological Critical Care")][1]/following-sibling::text())').getall()
            rfp_in_neuro = rfp_in_neuro1
            rfp_in_neuro2 = row.xpath(
                'normalize-space(.//*[contains(text(),"RFP in Neurological Critical Care")][1]/following-sibling::text())').getall()
            rfp_in_neuro3 = row.xpath(
                'normalize-space(.//*[contains(text(),"RFP in Neurological Critical Care")][1]/following-sibling::text())').getall()
            rfp_in_neuro4 = row.xpath(
                'normalize-space(.//*[contains(text(),"RFP in Neurological Critical Care")][1]/following-sibling::text())').getall()
            rfp_in_neuro5 = row.xpath(
                'normalize-space(.//*[contains(text(),"RFP in Neurological Critical Care")][1]/following-sibling::text())').getall()
            if len(rfp_in_neuro2[0]) > 0:
                rfp_in_neuro = f'{rfp_in_neuro1}, {rfp_in_neuro2}'
            if len(rfp_in_neuro3[0]) > 0:
                rfp_in_neuro = f'{rfp_in_neuro1}, {rfp_in_neuro2}, {rfp_in_neuro3}'
            if len(rfp_in_neuro4[0]) > 0:
                rfp_in_neuro = f'{rfp_in_neuro1}, {rfp_in_neuro2}, {rfp_in_neuro3}, {rfp_in_neuro4}'
            if len(rfp_in_neuro5[0]) > 0:
                rfp_in_neuro = f'{rfp_in_neuro1}, {rfp_in_neuro2}, {rfp_in_neuro3}, {rfp_in_neuro4}, {rfp_in_neuro5}'

            rfp_in_pedia1 = row.xpath(
                'normalize-space(.//*[contains(text(),"RFP in Pediatric Neurological Surgery")][1]/following-sibling::text())').getall()
            rfp_in_pedia = rfp_in_pedia1
            rfp_in_pedia2 = row.xpath(
                'normalize-space(.//*[contains(text(),"RFP in Pediatric Neurological Surgery")][2]/following-sibling::text())').getall()
            rfp_in_pedia3 = row.xpath(
                'normalize-space(.//*[contains(text(),"RFP in Pediatric Neurological Surgery")][3]/following-sibling::text())').getall()
            rfp_in_pedia4 = row.xpath(
                'normalize-space(.//*[contains(text(),"RFP in Pediatric Neurological Surgery")][4]/following-sibling::text())').getall()
            rfp_in_pedia5 = row.xpath(
                'normalize-space(.//*[contains(text(),"RFP in Pediatric Neurological Surgery")][5]/following-sibling::text())').getall()
            if len(rfp_in_pedia2[0]) > 0:
                rfp_in_pedia = f'{rfp_in_pedia1}, {rfp_in_pedia2}'
            if len(rfp_in_pedia3[0]) > 0:
                rfp_in_pedia = f'{rfp_in_pedia1}, {rfp_in_pedia2}, {rfp_in_pedia3}'
            if len(rfp_in_pedia4[0]) > 0:
                rfp_in_pedia = f'{rfp_in_pedia1}, {rfp_in_pedia2}, {rfp_in_pedia3}, {rfp_in_pedia4}'
            if len(rfp_in_pedia5[0]) > 0:
                rfp_in_pedia = f'{rfp_in_pedia1}, {rfp_in_pedia2}, {rfp_in_pedia3}, {rfp_in_pedia4}, {rfp_in_pedia5}'

            yield {
                'Neurosurgeon': name,
                'ABNS Certificate': abns_certificate,
                'RFP in CNS Endovascular Surgery': rfp_in_cns,
                'RFP in Neurological Critical Care': rfp_in_neuro,
                'RFP in Pediatric Neurological Surgery': rfp_in_pedia,
                'Certified': certified,
                'Lifetime': lifetime,
            }
