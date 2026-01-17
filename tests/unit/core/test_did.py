# Copyright 2024 ZhongXin Wang
# Licensed under the Apache License, Version 2.0

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../..'))

import pytest
from src.core.did import DID
from src.core.exceptions import DIDValidationError

class TestDID:
    def test_create_did(self):
        """Test creating a new DID."""
        did = DID.create(did_type="resident")
        assert did.did.startswith("did:xca:resident:")
        assert len(did.method_specific_id) == 32
    
    def test_parse_valid_did(self):
        """Test parsing a valid DID string."""
        did_str = "did:xca:resident:abc123"
        did = DID.parse(did_str)
        assert did.did == did_str
        assert did.did_type == "resident"
    
    def test_parse_invalid_did(self):
        """Test parsing an invalid DID string."""
        with pytest.raises(DIDValidationError):
            DID.parse("invalid:did:format")
    
    def test_parse_wrong_method(self):
        """Test parsing DID with wrong method."""
        with pytest.raises(DIDValidationError):
            DID.parse("did:other:resident:abc123")
    
    def test_generate_document(self):
        """Test generating a DID document."""
        did = DID.create()
        doc = did.generate_document()
        assert doc["id"] == did.did
        assert "verificationMethod" in doc
        assert "authentication" in doc
        assert doc["created"].endswith("Z")
    
    def test_did_equality(self):
        """Test DID equality comparison."""
        did1 = DID.parse("did:xca:resident:abc123")
        did2 = DID.parse("did:xca:resident:abc123")
        did3 = DID.parse("did:xca:device:xyz789")
        
        assert did1 == did2
        assert did1 != did3
        assert hash(did1) == hash(did2)
    
    def test_different_types(self):
        """Test creating different DID types."""
        resident_did = DID.create(did_type="resident")
        org_did = DID.create(did_type="organization")
        device_did = DID.create(did_type="device")
        
        assert resident_did.did_type == "resident"
        assert org_did.did_type == "organization"
        assert device_did.did_type == "device"
        assert "did:xca:resident:" in resident_did.did
        assert "did:xca:organization:" in org_did.did
