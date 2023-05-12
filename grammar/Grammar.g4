grammar Grammar;

INT : [0-9]+ ;
WS: [ \t\r\f]+ -> skip ;
NL: '\r'? '\n' -> skip;
Name: [a-zA-Z_][a-zA-Z_0-9]* ;
String: '"' .*? '"';

document
    : definition* EOF
    ;

definition
    : typeDefinition
    | queryDefinition
    ;

typeDefinition
    : objectTypeDefinition
    // | enumTypeDefinition
    ;

objectTypeDefinition
    : 'type' Name  '{' fieldsDefinition '}'
    ;

fieldsDefinition
    : (fieldDefinition ',')* fieldDefinition
    ;

fieldDefinition
    : Name paramsDefinition? ':' fieldType
    ;

fieldType
    : '[' Name '!' ? ']' '!'?
    |  Name '!'?
    ;

paramsDefinition
    : '(' (paramDefinition ',' )* paramDefinition ')'
    ;

paramDefinition
    : Name ':' fieldType
    ;

queryDefinition
    : 'query' selectionSet
    ;

selectionSet
    : '{' (field ',')* field '}'
    ;

field
    : Name params? selectionSet?
    ;

params
    : '(' (param ',')* param ')'
    ;

param
    : Name ':' value
    ;

value: INT | String ;
