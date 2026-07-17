from fastapi import HTTPException
from fastapi import status

class SecurityException:
    @staticmethod
    def unauthorised():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized"
        )
    
    @staticmethod
    def forbidden():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden"
        )
    