from mongoengine import Document, StringField, DateTimeField, ObjectIdField
from datetime import datetime

class Task(Document):
    task_id = ObjectIdField(required=True, primary_key=True)
    title = StringField(required=True, max_length=100)
    description = StringField()
    status = StringField(
        choices=["Pending", "In Progress", "Completed"],
        default="Pending"
    )
    priority = StringField(
        choices=["Low", "Medium", "High"],
        default="Medium"
    )
    created_by = StringField(required=True)
    assigned_to = StringField()
    due_date = DateTimeField()
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)
    
    meta={
        'collection': 'tasks',
        'indexes': [
            'task_id',
            'created_by',
            'assigned_to',
            'status',
            'priority',
            'due_date'
        ]
    }
