import scrapy


class JournalDataSpider(scrapy.Spider):
    name = 'journal_data'

    # Replace with  target URLs
    start_urls = [
        'https://www.scimagojr.com/journalsearch.php?q=28773&tip=sid&clean=0',
    ]


    def parse(self, response):
        # Locate the <h2> tag with "Information" and find all <a> tags under it
        information_section = response.xpath("//h2[contains(text(), 'Information')]/following-sibling::p")
        information_links = information_section.xpath(".//a/@href").extract()

        # Ensure we have exactly 3 columns for the links (pad with None if needed)
        links = information_links[:3]  # Get up to 3 links
        while len(links) < 3:
            links.append(None)  # Add None for missing links

        # Locate the text under <h2>Scope</h2>
        scope_section = response.xpath("//h2[contains(text(), 'Scope')]/following-sibling::text()").extract_first()
        scope_text = scope_section.strip() if scope_section else "N/A"

        # Yield the collected data, splitting links into separate fields
        yield {
            'url': response.url,
            'link1': links[0],
            'link2': links[1],
            'link3': links[2],
            'scope_text': scope_text
        }