from core.plugin.plugin import EncoderPlugin

class Plugin(EncoderPlugin):
    """
    Encodes a URL.

    Example:

        Input:
            abcdefghijklmnopqrstuvwxyz%0A%21%22%C2%A7%24%25%26/%28%29%3D%3F%C2%B4%60%0A0123456789%0A
        Output:
            abcdefghijklmnopqrstuvwxyz
            !"§$%&/()=?´`
            0123456789
    """

    def __init__(self, context):
        # Name, Author, Dependencies
        super().__init__('URL+', "Thomas Engel", ["urllib"])

    def run(self, text):
        import urllib.parse
        return urllib.parse.quote_plus(text.encode('utf-8', errors='surrogateescape'))
