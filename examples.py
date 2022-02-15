import LookupTables

#Some examples
print(LookupTables.EventID.getDescription("4625"))
print(LookupTables.Status.getDescription("0xC0368002"))
print(LookupTables.Error.getDescription("0x00003AA6"))
print(LookupTables.FailureReason.getDescription("%%2310"))

