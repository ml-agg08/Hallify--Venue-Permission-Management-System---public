# Venue/Hall Permission Management System Documentation

## Table of Contents
1. *Introduction*
2. *Project Concept & Background*
3. *User Roles & Workflow*
4. *System Features*
5. *Future Improvements*
6. *Screenshots*
7. *Setup Instructions*

---

## 1. Introduction
The Venue/Hall Permission Management System is designed to digitize and streamline the process of obtaining venue permissions in our college. This system eliminates the need for excessive paperwork, reduces miscommunication, and ensures transparency in venue allocation.

## 2. Project Concept & Background
As the lead of the TinkerHub TKMCE campus community, I and my team faced significant challenges in obtaining permissions for venues to conduct events. The traditional process involved running between departments, waiting for approvals, and handling paperwork, which often got lost or delayed. Other key issues included:
- Physical hassle of running between different authorities.
- Risk of losing paperwork and needing to start the process over.
- Payment required for obtaining multiple copies of permission letters.
- Miscommunication leading to multiple clubs booking the same venue simultaneously.

The need for an efficient, centralized, and paperless system was evident, leading to the development of this project.

## 3. User Roles & Workflow
### 3.1 Static Elements
- *Clubs:* Each club remains constant over time, but its representatives change.
- *Venues:* Venues are categorized into three types: 
  - *General Venues*
  - *Department Venues*
  - *Classroom Venues*

### 3.2 User Roles
#### 3.2.1 Club Representative
- Registers on the system, selects the role, and chooses a club.
- Only one club representative is allowed per club.
- If a user skips completing their profile, they will be redirected to finish it before proceeding.
- Can view the permission list (permitted and pending requests).
- Can check for scheduling clashes before submitting a request.
- If there is a clash, they cannot submit a request but can contact the conflicting club.
- Can submit a permission request including event details and venue details.
- Receives updates on permission status as approvals progress.

#### 3.2.2 Office Personnel
- Can register and choose the office personnel role.
- Can view all permission requests submitted by club representatives.
- Can approve or reject permission requests.
- Upon approval, the club representative’s view updates accordingly.
- Receives email notifications when new permission requests are submitted.

#### 3.2.3 Faculty Coordinator
- Each club has an assigned faculty coordinator.
- Registers, selects role, and associates with a club.
- Can view and approve only their club’s permission requests.
- Approval is required before moving to the next step.
- Receives email notifications for pending requests.

#### 3.2.4 Venue Faculty Coordinator
- Each venue has a designated venue faculty coordinator.
- Registers, selects role, and associates with a venue.
- Can view and approve permission requests for their venue.
- Approval is required before moving to the next step.
- Receives email notifications for pending requests.

#### 3.2.5 Venue Faculty Staff (For Department Venues Only)
- For department-type venues, once the venue faculty coordinator (e.g., department HoD) approves, the request is visible to the *venue faculty staff*.
- The venue faculty staff does not have approval authority but can access the permission details.
- They act as the point of contact, managing keys and logistical aspects of the venue.

#### 3.2.6 Security
- Multiple security personnel can register and choose their role.
- Can view approved permissions and ensure venue access accordingly.
- Their approval is required before a permission request is fully granted.
- Helps avoid venue closing issues due to miscommunication.

#### 3.2.7 Faculty (Independent Requests)
- Faculty members not associated with any club can create permission requests.
- Their requests require approval from the *Office Personnel, **Venue Faculty Coordinator, and **Security*.

## 4. System Features
- *Role-Based Access:* Different users see only the permissions relevant to their role.
- *Clash Detection:* Prevents scheduling conflicts between multiple club events.
- *Email Notifications:* Automatic notifications at each stage of approval.
- *Live Status Updates:* Users can track the progress of their permission requests.
- *Security View:* Security personnel can see approved events for better coordination.
- *Profile Completion Enforcement:* Ensures users fill in all required details before proceeding.

## 5. Future Improvements
1. *Permission Givers Can Leave Comments*
   - After approval or disapproval, permission givers can provide comments explaining their decision.
2. *Permission Requesters Can Cancel Permissions*
   - Club Representatives and Faculty can delete their permission requests before final approval.

## 6. Screenshots
(Placeholder for system UI screenshots—each feature section should be accompanied by a relevant image.)

## 7. Setup Instructions

### 🚀 Running the Project Locally

Follow these steps to set up and run the project:

### 1️⃣ Create a Virtual Environment
Run the following command:

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Create a .env File

In the root directory, create a `.env` file and add the following details:

```ini
# Secret Key
SECRET_KEY=your-secret-key

# Debug mode (set to False in production)
DEBUG=True

# Database Configuration
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=5432

# Email Configuration
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-email-password
```

### 4️⃣ Apply Migrations and Run the Server

```bash
python manage.py migrate
python manage.py runserver
```

Your Django app should now be running at [http://127.0.0.1:8000/](http://127.0.0.1:8000/). 🎉

