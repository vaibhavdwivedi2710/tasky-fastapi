from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

# --------------------------------------------
# 1. Create Task Request DTO
# --------------------------------------------

class CreateTaskRequestDTO(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = Field(default="Pending")
    priority: Optional[str] = Field(default="Medium")
    created_by: str
    assigned_to: Optional[str] = None
    due_date: Optional[datetime] = None


# --------------------------------------------
# 2. Create Task Response DTO
# --------------------------------------------

class CreateTaskResponseDTO(BaseModel):
    task_id: str
    message: str = "Task created successfully"


# --------------------------------------------
# 3. Get Task By ID Response DTO
# --------------------------------------------

class GetTaskByIdResponseDTO(BaseModel):
    task_id: str
    title: str
    description: Optional[str]
    status: str
    priority: str
    created_by: str
    assigned_to: Optional[str]
    due_date: Optional[datetime]
    created_at: datetime
    updated_at: datetime


# --------------------------------------------
# 4. Update Task Request DTO
# --------------------------------------------

class UpdateTaskRequestDTO(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[str]
    priority: Optional[str]
    assigned_to: Optional[str]
    due_date: Optional[datetime]


# --------------------------------------------
# 5. Update Task Response DTO
# --------------------------------------------

class UpdateTaskResponseDTO(BaseModel):
    task_id: str
    message: str = "Task updated successfully"


# --------------------------------------------
# 6. Delete Task Response DTO
# --------------------------------------------

class DeleteTaskResponseDTO(BaseModel):
    task_id: str
    message: str = "Task deleted successfully"


# --------------------------------------------
# 7. List Task Filters DTO (Optional Query Params)
# --------------------------------------------

class TaskFilterDTO(BaseModel):
    status: Optional[str] = None
    priority: Optional[str] = None
    created_by: Optional[str] = None
    assigned_to: Optional[str] = None


# --------------------------------------------
# 8. List Tasks Response DTO
# --------------------------------------------

class ListTasksResponseItemDTO(BaseModel):
    task_id: str
    title: str
    status: str
    priority: str
    assigned_to: Optional[str]
    due_date: Optional[datetime]
    created_at: datetime
    updated_at: datetime

class ListTasksResponseDTO(BaseModel):
    tasks: List[ListTasksResponseItemDTO]