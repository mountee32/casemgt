from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Document(Base):
    __tablename__ = "documents"
    
    document_id = Column(Integer, primary_key=True, index=True)
    case_id = Column(Integer, nullable=False)  # Removed ForeignKey for PoC
    title = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    document_type = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(Integer, nullable=False)  # Removed ForeignKey for PoC
