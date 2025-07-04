grammar Sample;

program: sentence;

sentence: VERB SUB ID+ E_Mask;

VERB: ('Could'|'Should'|'Can'|'Would');
SUB: ('he'|'she'|'they'|'we');
ID: [a-z] ;
E_Mask: '?';

WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines