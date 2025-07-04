grammar Sample;

program: command;

command: conditionalCommand | actionSentence;

conditionalCommand: ifCondition | whileCondition;

ifCondition: 'If' timeAttribute 'is' timeComparision Time 'then' actionSentence;
whileCondition: 'While' elementAttribute 'is' Comparision Integer 'do' actionSentence;

timeAttribute: 'the current time';
timeComparision: 'before' | 'after' | 'equal to';

elementAttribute: 'the'? IDENTIFIER+;
Comparision: 'above' | 'below' | 'equal to';

objectAttribute: 'the'? IDENTIFIER+ mediaType;
mediaType: ('video' | 'audio')?;

actionSentence: turnAction | setAction | editAction | playAction;
turnAction: ('Turn' | 'turn') ('on' | 'off') deviceNLocation;
setAction: ('Set' | 'set') elementAttribute 'to' Integer;
editAction: ('Increase'|'Decrease' | 'increase'|'decrease') deviceNLocation elementAttribute? 'by' Integer;
playAction: ('Play' | 'play') objectAttribute location;

deviceNLocation: device location?;
device: 'the'? IDENTIFIER+;
Prepositions: ('in' | 'on' | 'at');
location: Prepositions 'the'? ('classroom' | 'kitchen' | 'living room' | 'bedroom' | 'bathroom' | 'table') IDENTIFIER;

Integer: [0-9]+ ;
IDENTIFIER: [a-zA-Z0-9]+ ;

Time: [0-9][0-9]':'[0-9][0-9];
WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines