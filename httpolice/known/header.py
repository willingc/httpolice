# -*- coding: utf-8; -*-

from httpolice.common import Citation, FieldName, RFC
from httpolice.known.base import KnownDict
from httpolice.parse import anything, decode
from httpolice.syntax import (
    rfc3986,
    rfc5646,
    rfc7230,
    rfc7231,
    rfc7232,
    rfc7233,
    rfc7234,
)
from httpolice.syntax.common import integer


SINGLE = 1
MULTI = 2
SET_COOKIE = 3
CACHE_CONTROL = 4


def is_bad_for_connection(name):
    return known.get_info(name).get('bad_for_connection')

def is_bad_for_trailer(name):
    return known.get_info(name).get('bad_for_trailer')

def is_for_request(name):
    return known.get_info(name).get('for_request')

def is_for_response(name):
    return known.get_info(name).get('for_response')

def is_precondition(name):
    return known.get_info(name).get('precondition')

def is_proactive_conneg(name):
    return known.get_info(name).get('proactive_conneg')

def is_representation_metadata(name):
    return known.get_info(name).get('representation_metadata')

def rule_for(name):
    return known.get_info(name).get('rule')

def parser_for(name):
    return known.get_info(name).get('parser')


known = KnownDict([
 {'_': FieldName(u'A-IM'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Accept'),
  '_citations': [RFC(7231, section=(5, 3, 2))],
  'for_request': True,
  'for_response': False,
  'iana_status': 'standard',
  'parser': rfc7231.accept,
  'precondition': False,
  'proactive_conneg': True,
  'rule': MULTI},
 {'_': FieldName(u'Accept-Additions'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Accept-Charset'),
  '_citations': [RFC(7231, section=(5, 3, 3))],
  'for_request': True,
  'for_response': False,
  'iana_status': 'standard',
  'parser': rfc7231.accept_charset,
  'precondition': False,
  'proactive_conneg': True,
  'rule': MULTI},
 {'_': FieldName(u'Accept-Datetime'),
  '_citations': [RFC(7089)],
  'iana_status': 'informational'},
 {'_': FieldName(u'Accept-Encoding'),
  '_citations': [RFC(7231, section=(5, 3, 4)), RFC(7694, section=(3,))],
  'for_request': True,
  'for_response': True,         # RFC 7694
  'iana_status': 'standard',
  'parser': rfc7231.accept_encoding,
  'precondition': False,
  'proactive_conneg': True,
  'rule': MULTI},
 {'_': FieldName(u'Accept-Features'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Accept-Language'),
  '_citations': [RFC(7231, section=(5, 3, 5))],
  'for_request': True,
  'for_response': False,
  'iana_status': 'standard',
  'parser': rfc7231.accept_language,
  'precondition': False,
  'proactive_conneg': True,
  'rule': MULTI},
 {'_': FieldName(u'Accept-Patch'), '_citations': [RFC(5789)]},
 {'_': FieldName(u'Accept-Ranges'),
  '_citations': [RFC(7233, section=(2, 3))],
  'for_request': False,
  'for_response': True,
  'iana_status': 'standard',
  'parser': rfc7233.acceptable_ranges,
  'rule': SINGLE},
 {'_': FieldName(u'Age'),
  '_citations': [RFC(7234, section=(5, 1))],
  'bad_for_connection': True,
  'bad_for_trailer': True,
  'for_request': False,
  'for_response': True,
  'iana_status': 'standard',
  'parser': integer,
  'rule': SINGLE},
 {'_': FieldName(u'Allow'),
  '_citations': [RFC(7231, section=(7, 4, 1))],
  'for_request': False,
  'for_response': True,
  'iana_status': 'standard',
  'parser': rfc7230.comma_list(rfc7230.method),
  'rule': MULTI},
 {'_': FieldName(u'ALPN'),
  '_citations': [RFC(7639, section=(2,))],
  'iana_status': 'standard'},
 {'_': FieldName(u'Alternates'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Apply-To-Redirect-Ref'), '_citations': [RFC(4437)]},
 {'_': FieldName(u'Authentication-Info'),
  '_citations': [RFC(7615, section=(3,))],
  'iana_status': 'standard'},
 {'_': FieldName(u'Authorization'),
  '_citations': [RFC(7235, section=(4, 2))],
  'bad_for_trailer': True,
  'iana_status': 'standard'},
 {'_': FieldName(u'C-Ext'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'C-Man'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'C-Opt'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'C-PEP'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'C-PEP-Info'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Cache-Control'),
  '_citations': [RFC(7234, section=(5, 2))],
  'bad_for_connection': True,
  'bad_for_trailer': True,
  'for_request': True,
  'for_response': True,
  'iana_status': 'standard',
  'parser': rfc7230.comma_list1(rfc7234.cache_directive),
  'precondition': False,
  'proactive_conneg': False,
  'rule': CACHE_CONTROL},
 {'_': FieldName(u'CalDAV-Timezones'),
  '_citations': [],
  'iana_status': 'standard'},
 {'_': FieldName(u'Close'),
  '_citations': [RFC(7230, section=(8, 1))],
  'iana_status': 'reserved'},
 {'_': FieldName(u'Connection'),
  '_citations': [RFC(7230, section=(6, 1))],
  'for_request': True,
  'for_response': True,
  'iana_status': 'standard',
  'parser': rfc7230.comma_list1(rfc7230.connection_option),
  'precondition': False,
  'proactive_conneg': False,
  'rule': MULTI},
 {'_': FieldName(u'Content-Base'),
  '_citations': [RFC(2068), RFC(2616)],
  'iana_status': 'obsoleted'},
 {'_': FieldName(u'Content-Disposition'),
  '_citations': [RFC(6266)],
  'iana_status': 'standard'},
 {'_': FieldName(u'Content-Encoding'),
  '_citations': [RFC(7231, section=(3, 1, 2, 2))],
  'bad_for_connection': True,
  'bad_for_trailer': True,
  'iana_status': 'standard',
  'parser': rfc7230.comma_list1(rfc7231.content_coding),
  'precondition': False,
  'proactive_conneg': False,
  'representation_metadata': True,
  'rule': MULTI},
 {'_': FieldName(u'Content-ID'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Content-Language'),
  '_citations': [RFC(7231, section=(3, 1, 3, 2))],
  'bad_for_connection': True,
  'iana_status': 'standard',
  'parser': rfc7230.comma_list1(rfc5646.language_tag),
  'precondition': False,
  'proactive_conneg': False,
  'representation_metadata': True,
  'rule': MULTI},
 {'_': FieldName(u'Content-Length'),
  '_citations': [RFC(7230, section=(3, 3, 2))],
  'bad_for_trailer': True,
  'for_request': True,
  'for_response': True,
  'iana_status': 'standard',
  'parser': integer,
  'precondition': False,
  'proactive_conneg': False,
  'rule': SINGLE},
 {'_': FieldName(u'Content-Location'),
  '_citations': [RFC(7231, section=(3, 1, 4, 2))],
  'iana_status': 'standard',
  'parser': rfc3986.absolute_uri | rfc7230.partial_uri,
  'precondition': False,
  'proactive_conneg': False,
  'representation_metadata': True,
  'rule': SINGLE},
 {'_': FieldName(u'Content-MD5'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Content-Range'),
  '_citations': [RFC(7233, section=(4, 2))],
  'bad_for_connection': True,
  'bad_for_trailer': True,
  'for_request': False,
  'for_response': True,
  'iana_status': 'standard',
  'parser': rfc7233.content_range,
  'rule': SINGLE},
 {'_': FieldName(u'Content-Script-Type'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Content-Style-Type'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Content-Type'),
  '_citations': [RFC(7231, section=(3, 1, 1, 5))],
  'bad_for_trailer': True,
  'iana_status': 'standard',
  'parser': rfc7231.media_type,
  'precondition': False,
  'proactive_conneg': False,
  'representation_metadata': True,
  'rule': SINGLE},
 {'_': FieldName(u'Content-Version'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Cookie'),
  '_citations': [RFC(6265)],
  'iana_status': 'standard'},
 {'_': FieldName(u'Cookie2'),
  '_citations': [RFC(2965), RFC(6265)],
  'iana_status': 'obsoleted'},
 {'_': FieldName(u'DASL'),
  '_citations': [RFC(5323)],
  'iana_status': 'standard'},
 {'_': FieldName(u'DAV'),
  '_citations': [RFC(4918)],
  'iana_status': 'standard'},
 {'_': FieldName(u'Date'),
  '_citations': [RFC(7231, section=(7, 1, 1, 2))],
  'bad_for_trailer': True,
  'for_request': True,
  'for_response': True,
  'iana_status': 'standard',
  'precondition': False,
  'proactive_conneg': False,
  'parser': rfc7231.http_date,
  'rule': SINGLE},
 {'_': FieldName(u'Default-Style'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Delta-Base'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Depth'),
  '_citations': [RFC(4918)],
  'iana_status': 'standard'},
 {'_': FieldName(u'Derived-From'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Destination'),
  '_citations': [RFC(4918)],
  'iana_status': 'standard'},
 {'_': FieldName(u'Differential-ID'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Digest'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'ETag'),
  '_citations': [RFC(7232, section=(2, 3))],
  'bad_for_connection': True,
  'for_request': False,
  'for_response': True,
  'iana_status': 'standard',
  'parser': rfc7232.entity_tag,
  'representation_metadata': True,
  'rule': SINGLE},
 {'_': FieldName(u'Expect'),
  '_citations': [RFC(7231, section=(5, 1, 1))],
  'bad_for_trailer': True,
  'for_request': True,
  'for_response': False,
  'iana_status': 'standard',
  'parser': anything,
  'precondition': False,
  'proactive_conneg': False,
  'rule': SINGLE},
 {'_': FieldName(u'Expires'),
  '_citations': [RFC(7234, section=(5, 3))],
  'bad_for_connection': True,
  'bad_for_trailer': True,
  'for_request': False,
  'for_response': True,
  'iana_status': 'standard',
  'parser': rfc7231.http_date,
  'rule': SINGLE},
 {'_': FieldName(u'Ext'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Forwarded'),
  '_citations': [RFC(7239)],
  'iana_status': 'standard'},
 {'_': FieldName(u'From'),
  '_citations': [RFC(7231, section=(5, 5, 1))],
  'for_request': True,
  'for_response': False,
  'iana_status': 'standard',
  # I'm not parsing the full RFC 5322 ``<mailbox>``, not right now.
  'parser': anything,
  'precondition': False,
  'proactive_conneg': False,
  'rule': SINGLE},
 {'_': FieldName(u'GetProfile'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Hobareg'),
  '_citations': [RFC(7486, section=(6, 1, 1))],
  'iana_status': 'experimental'},
 {'_': FieldName(u'Host'),
  '_citations': [RFC(7230, section=(5, 4))],
  'bad_for_trailer': True,
  'for_request': True,
  'for_response': False,
  'iana_status': 'standard',
  'parser': rfc7230.host,
  'precondition': False,
  'proactive_conneg': False,
  'rule': SINGLE},
 {'_': FieldName(u'HTTP2-Settings'),
  '_citations': [RFC(7540, section=(3, 2, 1))],
  'iana_status': 'standard'},
 {'_': FieldName(u'IM'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'If'),
  '_citations': [RFC(4918, section=(10, 4))],
  'bad_for_trailer': True,
  'iana_status': 'standard',
  'precondition': True},
 {'_': FieldName(u'If-Match'),
  '_citations': [RFC(7232, section=(3, 1))],
  'bad_for_trailer': True,
  'for_request': True,
  'for_response': False,
  'iana_status': 'standard',
  'parser': decode('*') | rfc7230.comma_list1(rfc7232.entity_tag),
  'precondition': True,
  'proactive_conneg': False,
  'rule': SINGLE},
 {'_': FieldName(u'If-Modified-Since'),
  '_citations': [RFC(7232, section=(3, 3))],
  'bad_for_trailer': True,
  'for_request': True,
  'for_response': False,
  'iana_status': 'standard',
  'parser': rfc7231.http_date,
  'precondition': True,
  'proactive_conneg': False,
  'rule': SINGLE},
 {'_': FieldName(u'If-None-Match'),
  '_citations': [RFC(7232, section=(3, 2))],
  'bad_for_trailer': True,
  'for_request': True,
  'for_response': False,
  'iana_status': 'standard',
  'parser': decode('*') | rfc7230.comma_list1(rfc7232.entity_tag),
  'precondition': True,
  'proactive_conneg': False,
  'rule': SINGLE},
 {'_': FieldName(u'If-Range'),
  '_citations': [RFC(7233, section=(3, 2))],
  'bad_for_trailer': True,
  'for_request': True,
  'for_response': False,
  'iana_status': 'standard',
  'parser': rfc7232.entity_tag | rfc7231.http_date,
  'precondition': False,
  'proactive_conneg': False,
  'rule': SINGLE},
 {'_': FieldName(u'If-Schedule-Tag-Match'),
  'bad_for_trailer': True,
  '_citations': [RFC(6638, section=(8, 3))],
  'iana_status': 'standard',
  'precondition': True},
 {'_': FieldName(u'If-Unmodified-Since'),
  '_citations': [RFC(7232, section=(3, 4))],
  'bad_for_trailer': True,
  'for_request': True,
  'for_response': False,
  'iana_status': 'standard',
  'parser': rfc7231.http_date,
  'precondition': True,
  'proactive_conneg': False,
  'rule': SINGLE},
 {'_': FieldName(u'Keep-Alive'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Label'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Last-Modified'),
  '_citations': [RFC(7232, section=(2, 2))],
  'bad_for_connection': True,
  'for_request': False,
  'for_response': True,
  'iana_status': 'standard',
  'parser': rfc7231.http_date,
  'representation_metadata': True,
  'rule': SINGLE},
 {'_': FieldName(u'Link'), '_citations': [RFC(5988)]},
 {'_': FieldName(u'Location'),
  '_citations': [RFC(7231, section=(7, 1, 2))],
  'bad_for_trailer': True,
  'for_request': False,
  'for_response': True,
  'iana_status': 'standard',
  'parser': rfc3986.uri_reference,
  'rule': SINGLE},
 {'_': FieldName(u'Lock-Token'),
  '_citations': [RFC(4918)],
  'iana_status': 'standard'},
 {'_': FieldName(u'Man'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Max-Forwards'),
  '_citations': [RFC(7231, section=(5, 1, 2))],
  'bad_for_trailer': True,
  'for_request': True,
  'for_response': False,
  'iana_status': 'standard',
  'parser': integer,
  'precondition': False,
  'proactive_conneg': False,
  'rule': SINGLE},
 {'_': FieldName(u'Memento-Datetime'),
  '_citations': [RFC(7089)],
  'iana_status': 'informational'},
 {'_': FieldName(u'Meter'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'MIME-Version'),
  '_citations': [RFC(7231, appendix=('A', 1))],
  'iana_status': 'standard',
  'precondition': False,
  'proactive_conneg': False},
 {'_': FieldName(u'Negotiate'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Opt'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Ordering-Type'),
  '_citations': [RFC(4229)],
  'iana_status': 'standard'},
 {'_': FieldName(u'Origin'),
  '_citations': [RFC(6454)],
  'iana_status': 'standard'},
 {'_': FieldName(u'Overwrite'),
  '_citations': [RFC(4918)],
  'iana_status': 'standard'},
 {'_': FieldName(u'P3P'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'PEP'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'PICS-Label'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Pep-Info'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Position'),
  '_citations': [RFC(4229)],
  'iana_status': 'standard'},
 {'_': FieldName(u'Pragma'),
  '_citations': [RFC(7234, section=(5, 4))],
  'bad_for_trailer': True,
  'iana_status': 'standard',
  'precondition': False,
  'proactive_conneg': False},
 {'_': FieldName(u'Prefer'),
  '_citations': [RFC(7240)],
  'iana_status': 'standard'},
 {'_': FieldName(u'Preference-Applied'),
  '_citations': [RFC(7240)],
  'iana_status': 'standard'},
 {'_': FieldName(u'ProfileObject'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Protocol'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Protocol-Info'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Protocol-Query'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Protocol-Request'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Proxy-Authenticate'),
  '_citations': [RFC(7235, section=(4, 3))],
  'iana_status': 'standard'},
 {'_': FieldName(u'Proxy-Authentication-Info'),
  '_citations': [RFC(7615, section=(4,))],
  'iana_status': 'standard'},
 {'_': FieldName(u'Proxy-Authorization'),
  '_citations': [RFC(7235, section=(4, 4))],
  'bad_for_trailer': True,
  'iana_status': 'standard'},
 {'_': FieldName(u'Proxy-Features'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Proxy-Instruction'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Public'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Public-Key-Pins'),
  '_citations': [RFC(7469)],
  'iana_status': 'standard'},
 {'_': FieldName(u'Public-Key-Pins-Report-Only'),
  '_citations': [RFC(7469)],
  'iana_status': 'standard'},
 {'_': FieldName(u'Range'),
  '_citations': [RFC(7233, section=(3, 1))],
  'bad_for_trailer': True,
  'for_request': True,
  'for_response': False,
  'iana_status': 'standard',
  'parser': rfc7233.range,
  'precondition': False,
  'proactive_conneg': False,
  'rule': SINGLE},
 {'_': FieldName(u'Redirect-Ref'), '_citations': [RFC(4437)]},
 {'_': FieldName(u'Referer'),
  '_citations': [RFC(7231, section=(5, 5, 2))],
  'for_request': True,
  'for_response': False,
  'iana_status': 'standard',
  'parser': rfc3986.absolute_uri | rfc7230.partial_uri,
  'precondition': False,
  'proactive_conneg': False,
  'rule': SINGLE},
 {'_': FieldName(u'Retry-After'),
  '_citations': [RFC(7231, section=(7, 1, 3))],
  'bad_for_trailer': True,
  'for_request': False,
  'for_response': True,
  'iana_status': 'standard',
  'parser': rfc7231.http_date | integer,
  'rule': SINGLE},
 {'_': FieldName(u'Safe'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Schedule-Reply'),
  '_citations': [RFC(6638)],
  'iana_status': 'standard'},
 {'_': FieldName(u'Schedule-Tag'),
  '_citations': [RFC(6638)],
  'iana_status': 'standard'},
 {'_': FieldName(u'Sec-WebSocket-Accept'),
  '_citations': [RFC(6455)],
  'iana_status': 'standard'},
 {'_': FieldName(u'Sec-WebSocket-Extensions'),
  '_citations': [RFC(6455)],
  'iana_status': 'standard'},
 {'_': FieldName(u'Sec-WebSocket-Key'),
  '_citations': [RFC(6455)],
  'iana_status': 'standard'},
 {'_': FieldName(u'Sec-WebSocket-Protocol'),
  '_citations': [RFC(6455)],
  'iana_status': 'standard'},
 {'_': FieldName(u'Sec-WebSocket-Version'),
  '_citations': [RFC(6455)],
  'iana_status': 'standard'},
 {'_': FieldName(u'Security-Scheme'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Server'),
  '_citations': [RFC(7231, section=(7, 4, 2))],
  'for_request': False,
  'for_response': True,
  'iana_status': 'standard',
  'parser': rfc7231.server,
  'rule': SINGLE},
 {'_': FieldName(u'Set-Cookie'),
  '_citations': [RFC(6265)],
  'iana_status': 'standard',
  'rule': SET_COOKIE},
 {'_': FieldName(u'Set-Cookie2'),
  '_citations': [RFC(2965), RFC(6265)],
  'iana_status': 'obsoleted'},
 {'_': FieldName(u'SetProfile'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'SLUG'),
  '_citations': [RFC(5023)],
  'iana_status': 'standard'},
 {'_': FieldName(u'SoapAction'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Status-URI'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Strict-Transport-Security'),
  '_citations': [RFC(6797)],
  'iana_status': 'standard'},
 {'_': FieldName(u'Surrogate-Capability'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Surrogate-Control'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'TCN'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'TE'),
  '_citations': [RFC(7230, section=(4, 3))],
  'bad_for_trailer': True,
  'for_request': True,
  'for_response': False,
  'iana_status': 'standard',
  'parser': rfc7230.comma_list(rfc7230.t_codings),
  'precondition': False,
  'proactive_conneg': False,
  'rule': MULTI},
 {'_': FieldName(u'Timeout'),
  '_citations': [RFC(4918)],
  'iana_status': 'standard'},
 {'_': FieldName(u'Trailer'),
  '_citations': [RFC(7230, section=(4, 4))],
  'bad_for_trailer': True,
  'iana_status': 'standard',
  'parser': rfc7230.comma_list1(rfc7230.field_name),
  'precondition': False,
  'proactive_conneg': False,
  'rule': MULTI},
 {'_': FieldName(u'Transfer-Encoding'),
  '_citations': [RFC(7230, section=(3, 3, 1))],
  'bad_for_trailer': True,
  'for_request': True,
  'for_response': True,
  'iana_status': 'standard',
  'parser': rfc7230.comma_list1(rfc7230.transfer_coding),
  'precondition': False,
  'proactive_conneg': False,
  'rule': MULTI},
 {'_': FieldName(u'URI'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Upgrade'),
  '_citations': [RFC(7230, section=(6, 7))],
  'for_request': True,
  'for_response': True,
  'iana_status': 'standard',
  'parser': rfc7230.comma_list1(rfc7230.protocol),
  'precondition': False,
  'proactive_conneg': False,
  'rule': MULTI},
 {'_': FieldName(u'User-Agent'),
  '_citations': [RFC(7231, section=(5, 5, 3))],
  'for_request': True,
  'for_response': False,
  'iana_status': 'standard',
  'parser': rfc7231.user_agent,
  'precondition': False,
  'proactive_conneg': False,
  'rule': SINGLE},
 {'_': FieldName(u'Variant-Vary'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Vary'),
  '_citations': [RFC(7231, section=(7, 1, 4))],
  'bad_for_connection': True,
  'bad_for_trailer': True,
  'for_request': False,
  'for_response': True,
  'iana_status': 'standard',
  'parser': decode('*') | rfc7230.comma_list1(rfc7230.field_name),
  'rule': SINGLE},
 {'_': FieldName(u'Via'),
  '_citations': [RFC(7230, section=(5, 7, 1))],
  'for_request': True,
  'for_response': True,
  'iana_status': 'standard',
  'parser': rfc7230.via,
  'precondition': False,
  'proactive_conneg': False,
  'rule': MULTI},
 {'_': FieldName(u'WWW-Authenticate'),
  '_citations': [RFC(7235, section=(4, 1))],
  'iana_status': 'standard'},
 {'_': FieldName(u'Want-Digest'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Warning'),
  '_citations': [RFC(7234, section=(5, 5))],
  'bad_for_connection': True,
  'bad_for_trailer': True,
  'iana_status': 'standard'},
 {'_': FieldName(u'X-Frame-Options'),
  '_citations': [RFC(7034)],
  'iana_status': 'informational'},
 {'_': FieldName(u'Access-Control'),
  '_citations': [Citation('W3C Web Application Formats Working Group',
                          'http://www.w3.org/2006/appformats/')],
  'iana_status': 'deprecated'},
 {'_': FieldName(u'Access-Control-Allow-Credentials'),
  '_citations': [Citation('W3C Web Application Formats Working Group',
                          'http://www.w3.org/2006/appformats/')]},
 {'_': FieldName(u'Access-Control-Allow-Headers'),
  '_citations': [Citation('W3C Web Application Formats Working Group',
                          'http://www.w3.org/2006/appformats/')]},
 {'_': FieldName(u'Access-Control-Allow-Methods'),
  '_citations': [Citation('W3C Web Application Formats Working Group',
                          'http://www.w3.org/2006/appformats/')]},
 {'_': FieldName(u'Access-Control-Allow-Origin'),
  '_citations': [Citation('W3C Web Application Formats Working Group',
                          'http://www.w3.org/2006/appformats/')]},
 {'_': FieldName(u'Access-Control-Max-Age'),
  '_citations': [Citation('W3C Web Application Formats Working Group',
                          'http://www.w3.org/2006/appformats/')]},
 {'_': FieldName(u'Access-Control-Request-Method'),
  '_citations': [Citation('W3C Web Application Formats Working Group',
                          'http://www.w3.org/2006/appformats/')]},
 {'_': FieldName(u'Access-Control-Request-Headers'),
  '_citations': [Citation('W3C Web Application Formats Working Group',
                          'http://www.w3.org/2006/appformats/')]},
 {'_': FieldName(u'Compliance'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Content-Transfer-Encoding'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Cost'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'EDIINT-Features'), '_citations': [RFC(6017)]},
 {'_': FieldName(u'Message-ID'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Method-Check'),
  '_citations': [Citation('W3C Web Application Formats Working Group',
                          'http://www.w3.org/2006/appformats/')],
  'iana_status': 'deprecated'},
 {'_': FieldName(u'Method-Check-Expires'),
  '_citations': [Citation('W3C Web Application Formats Working Group',
                          'http://www.w3.org/2006/appformats/')],
  'iana_status': 'deprecated'},
 {'_': FieldName(u'Non-Compliance'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Optional'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Referer-Root'),
  '_citations': [Citation('W3C Web Application Formats Working Group',
                          'http://www.w3.org/2006/appformats/')],
  'iana_status': 'deprecated'},
 {'_': FieldName(u'Resolution-Hint'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Resolver-Location'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'SubOK'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Subst'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Title'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'UA-Color'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'UA-Media'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'UA-Pixels'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'UA-Resolution'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'UA-Windowpixels'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'Version'), '_citations': [RFC(4229)]},
 {'_': FieldName(u'X-Device-Accept'),
  '_citations': [Citation('W3C Mobile Web Best Practices Working Group',
                          'http://www.w3.org/2005/MWI/BPWG/')]},
 {'_': FieldName(u'X-Device-Accept-Charset'),
  '_citations': [Citation('W3C Mobile Web Best Practices Working Group',
                          'http://www.w3.org/2005/MWI/BPWG/')]},
 {'_': FieldName(u'X-Device-Accept-Encoding'),
  '_citations': [Citation('W3C Mobile Web Best Practices Working Group',
                          'http://www.w3.org/2005/MWI/BPWG/')]},
 {'_': FieldName(u'X-Device-Accept-Language'),
  '_citations': [Citation('W3C Mobile Web Best Practices Working Group',
                          'http://www.w3.org/2005/MWI/BPWG/')]},
 {'_': FieldName(u'X-Device-User-Agent'),
  '_citations': [Citation('W3C Mobile Web Best Practices Working Group',
                          'http://www.w3.org/2005/MWI/BPWG/')]}
 ],
 extra_info=['bad_for_connection', 'bad_for_trailer',
             'for_request', 'for_response', 'iana_status',
             'parser', 'precondition', 'proactive_conneg',
             'representation_metadata', 'rule']
)
