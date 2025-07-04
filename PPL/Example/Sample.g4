grammar Sample;

program: sentence;

sentence: ARE ID E_Mask;

ARE: 'Are';
ID: [a-z]+ ;
E_Mask: '?';

WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines