grammar Sample;

program: actionSentence;

actionSentence: TURN (ON | OFF) device  | SET device TO NUMBER  | (INCREASE | DECREASE) device BRIGHTNESS BY NUMBER | PLAY device IN location;
device: THE? IDENTIFIER+;
location: KITCHEN | (LIVING ROOM) | BEDROOM | BATHROOM;

SET: 'Set';
INCREASE: 'Increase';
DECREASE: 'Decrease';
PLAY: 'Play';
TURN: 'Turn';
ON: 'on';
OFF: 'off';
TO: 'to';
BRIGHTNESS: 'brightness';
BY: 'by';
IN: 'in';
THE: 'the';

KITCHEN: 'kitchen';
LIVING: 'living';
ROOM: 'room';
BEDROOM: 'bedroom';
BATHROOM: 'bathroom';

NUMBER: [0-9]+ ;
IDENTIFIER: [a-z]+ ;

WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines