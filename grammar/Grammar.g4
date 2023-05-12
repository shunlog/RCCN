grammar Grammar;

INT : [0-9]+ ;
WS: [ \t\r\f]+ -> skip ;
NL: '\r'? '\n' -> skip;
Name: [a-zA-Z_][a-zA-Z_0-9]* ;
String: '"' .*? '"';

document
    : typeDefinition+  field* EOF
    ;

typeDefinition
    : 'type' Name  fieldDefinitions  # objectTypeDefinition
    // | enumTypeDefinition
    ;

fieldDefinitions
    : '{' (fieldDefinition ',')* fieldDefinition '}'
    ;

fieldDefinition
    : Name paramDefinitions? ':' fieldType
    ;

fieldType
    :  Name '!'?
    | '[' Name '!'? ']' '!'?
    ;

paramDefinitions
    : '(' (paramDefinition ',' )* paramDefinition ')'
    ;

paramDefinition
    : Name ':' fieldType
    ;

field
    : Name params? selectionSet?
    ;

selectionSet
    : '{' (field ',')* field '}'
    ;

params
    : '(' (param ',')* param ')'
    ;

param
    : Name ':' value
    ;

value: INT | String ;
