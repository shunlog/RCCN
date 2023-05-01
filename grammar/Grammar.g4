grammar Grammar;

INT : [0-9]+ ;
WS: [ \t\r\f]+ -> skip ;
NL: '\r'? '\n' -> skip;
Name: [a-zA-Z_][a-zA-Z_0-9]* ;

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
    : Name params? ':' Name
    ;

params
    : '(' (param ',' )* param ')'
    ;

param
    : Name ':' Name
    ;

queryDefinition
    : 'query' Name  selectionSet
    ;

selectionSet
    : '{' fields '}'
    ;

fields
    : (field ',')* field
    ;

field
    : Name
    | Name  selectionSet
    ;
