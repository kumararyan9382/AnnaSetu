"""
Pydantic Models & Request Schemas for AnnaSetu
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class FarmerBookingRequest(BaseModel):
    farmer_name: str = Field(..., example="Ramesh Kumar")
    phone: str = Field(..., min_length=10, max_length=15, example="9876543210")
    village: str = Field(..., example="Taraori")
    district: str = Field(..., example="Karnal")
    state: str = Field(default="Haryana")
    crop_name: str = Field(..., example="Wheat (गेहूं)")
    estimated_quantity_qtl: float = Field(..., gt=0, example=45.0)
    vehicle_type: str = Field(default="Tractor Trolley (ट्रैक्टर ट्रॉली)")
    vehicle_number: Optional[str] = Field(default="HR-05-AB-1234")
    center_id: str = Field(..., example="CTR-001")
    scheduled_slot: Optional[str] = Field(default="09:00 AM - 11:00 AM")
    aadhaar_mask: Optional[str] = Field(default="XXXX-XXXX-1234")

class StageAdvanceRequest(BaseModel):
    to_stage: str = Field(..., example="WEIGHBRIDGE")
    operator_name: Optional[str] = Field(default="Mandi Officer")
    gross_weight_kg: Optional[float] = None
    tare_weight_kg: Optional[float] = None
    moisture_percent: Optional[float] = None
    foreign_matter_percent: Optional[float] = None
    quality_grade: Optional[str] = None
    notes: Optional[str] = None

class CenterCapacityUpdateRequest(BaseModel):
    active_weighbridges: int = Field(..., ge=1, le=10)
    active_quality_labs: int = Field(..., ge=1, le=10)
    congestion_status: str = Field(default="Smooth")
    is_active: bool = Field(default=True)

class VoiceQueryRequest(BaseModel):
    query: str = Field(..., example="9876543210")
    language: Optional[str] = Field(default="hi")

class SimulationActionRequest(BaseModel):
    action: str = Field(..., example="advance_all_queues")
    center_id: Optional[str] = None
