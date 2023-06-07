grammar Grammar;

Int : [0-9]+ ;
WS: [ \t\r\f]+ -> skip ;
NL: '\r'? '\n' -> skip;
Name: [a-zA-Z_][a-zA-Z_0-9]* ;
String: '"' .*? '"';
boolean: 'true' | 'false';

value: Int | String | boolean ;

document
    : typeDefinition+  field* EOF
    ;

// Schema definition

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
    :  Name
    | '[' Name ']'
    ;

paramDefinitions
    : '(' (paramDefinition ',' )* paramDefinition ')'
    ;

paramDefinition
    : Name ':' fieldType
    ;

// Queries

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
