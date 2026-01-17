python
   # Copyright 2024 [替换为您的姓名或ID]
   # Licensed under the Apache License, Version 2.0
   
   """Custom exceptions for the Civilization OS."""
   
   class CivilizationOSError(Exception):
       """Base exception for all Civilization OS errors."""
       pass
   
   class DIDValidationError(CivilizationOSError):
       """Raised when a DID validation fails."""
       pass
   
   class DIDNotFoundError(CivilizationOSError):
       """Raised when a DID cannot be resolved."""
       pass
