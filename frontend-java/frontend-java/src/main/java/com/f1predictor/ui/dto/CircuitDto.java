package com.f1predictor.ui.dto;

public class CircuitDto {
    private Integer circuit_id;
    private String circuit_ref;
    private String name;
    private String location;
    private String country;
    private Double lat;
    private Double lng;

    public Integer getCircuit_id() { return circuit_id; }
    public void setCircuit_id(Integer circuit_id) { this.circuit_id = circuit_id; }

    public String getCircuit_ref() { return circuit_ref; }
    public void setCircuit_ref(String circuit_ref) { this.circuit_ref = circuit_ref; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getLocation() { return location; }
    public void setLocation(String location) { this.location = location; }

    public String getCountry() { return country; }
    public void setCountry(String country) { this.country = country; }

    public Double getLat() { return lat; }
    public void setLat(Double lat) { this.lat = lat; }

    public Double getLng() { return lng; }
    public void setLng(Double lng) { this.lng = lng; }
}