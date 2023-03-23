grammar Grammar;

INT : [0-9]+ ;
WS: [ \t\r\f]+ -> skip ;
COLON : ':' ;
NL: '\r'? '\n';
TYPE: 'type';
QUERY: 'query';
Name: [a-zA-Z_][a-zA-Z_0-9]* ;
INDENT: '{';
DEDENT: '}';

document
    : definition* EOF
    ;

definition
    : typeDefinition NL*
    | queryDefinition NL*
    ;

typeDefinition
    : objectTypeDefinition
    // | enumTypeDefinition
    ;

objectTypeDefinition
    : TYPE Name ':' NL* INDENT fieldsDefinition DEDENT
    ;

fieldsDefinition
    : fieldDefinition*
    ;

fieldDefinition
    : Name params? ':' Name NL*
    ;

params
    : '(' NL* (param ',' NL*)* param NL*')'
    ;

param
    : Name ':' Name
    ;

queryDefinition
    : QUERY Name ':' NL* selectionSet
    ;

selectionSet
    : INDENT fields NL* DEDENT
    ;

fields
    : field*
    ;

field
    : Name NL*
    | Name ':' NL* selectionSet
    ;
