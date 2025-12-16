from backend.db.session import SessionLocal
from backend.models.user import User
from sqlalchemy import or_

def createAccount(userName: str, email: str, password: str):

    db = SessionLocal()

    try:
        # 1. CHECK: Look for any user with the same username OR email
        existing_user = db.query(User).filter(
            or_(User.username == userName, User.email == email)
        ).first()

        if existing_user:
            # We found a match, so we stop here
            if existing_user.username == userName:
                print(f"Error: The username '{userName}' is already taken.")
            else:
                print(f"Error: The email '{email}' is already in use.")
            return None
        new_user = User(
            username=userName,
            email=email,
            password=password
        )

        db.add(new_user)

        db.commit()

        db.refresh(new_user)
        
        print(f"User created with ID: {new_user.id}")
        return new_user
    
    except Exception as e:
        print(f"Error creating account: {e}")
        db.rollback() # Important: Undo changes if there's an error
        return None
        
    finally:
        db.close() # Important:

