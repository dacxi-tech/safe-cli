import re

from pygments.lexers.shell import BashLexer
from pygments.token import Keyword, Name, Text, Token


class SafeLexer(BashLexer):
    name = 'SafeLexer'
    aliases = ['safe_lexer']

    ADDRESS = r'^0x[aA-zZ,0-9]{40}$|^0x[aA-zZ,0-9]{62}$'
    EXTRA_KEYWORDS = {'refresh', 'get_nonce', 'get_owners', 'get_threshold', 'show_cli_owners',
                      'load_cli_owners', 'unload_cli_owners', 'add_owner', 'change_threshold', 'remove_owner',
                      'change_master_copy', 'send_ether', 'send_erc20', 'send_erc721'}

    def get_tokens_unprocessed(self, text: str) -> (int, Token, str):
        for index, token, value in BashLexer.get_tokens_unprocessed(self, text):
            if token is Text and value in self.EXTRA_KEYWORDS:
                yield index, Name.Builtin, value
            elif token is Text and re.search(self.ADDRESS, value):
                yield index, Keyword, value
            else:
                yield index, token, value
