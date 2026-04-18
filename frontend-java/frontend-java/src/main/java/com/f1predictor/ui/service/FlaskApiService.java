package com.f1predictor.ui.service;

import com.f1predictor.ui.dto.*;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.Collections;
import java.util.List;

@Service
public class FlaskApiService {

    private final RestTemplate restTemplate;

    @Value("${flask.api.base-url}")
    private String flaskBaseUrl;

    public FlaskApiService(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    public List<DriverDto> getDrivers() {
        ResponseEntity<List<DriverDto>> response = restTemplate.exchange(
                flaskBaseUrl + "/drivers",
                HttpMethod.GET,
                null,
                new ParameterizedTypeReference<List<DriverDto>>() {}
        );
        return response.getBody() != null ? response.getBody() : Collections.emptyList();
    }

    public List<ConstructorDto> getConstructors() {
        ResponseEntity<List<ConstructorDto>> response = restTemplate.exchange(
                flaskBaseUrl + "/constructors",
                HttpMethod.GET,
                null,
                new ParameterizedTypeReference<List<ConstructorDto>>() {}
        );
        return response.getBody() != null ? response.getBody() : Collections.emptyList();
    }

    public List<CircuitDto> getCircuits() {
        ResponseEntity<List<CircuitDto>> response = restTemplate.exchange(
                flaskBaseUrl + "/circuits",
                HttpMethod.GET,
                null,
                new ParameterizedTypeReference<List<CircuitDto>>() {}
        );
        return response.getBody() != null ? response.getBody() : Collections.emptyList();
    }

    public List<RaceDto> getRaces() {
        ResponseEntity<List<RaceDto>> response = restTemplate.exchange(
                flaskBaseUrl + "/races",
                HttpMethod.GET,
                null,
                new ParameterizedTypeReference<List<RaceDto>>() {}
        );
        return response.getBody() != null ? response.getBody() : Collections.emptyList();
    }

    public List<ResultDto> getResults() {
        ResponseEntity<List<ResultDto>> response = restTemplate.exchange(
                flaskBaseUrl + "/results",
                HttpMethod.GET,
                null,
                new ParameterizedTypeReference<List<ResultDto>>() {}
        );
        return response.getBody() != null ? response.getBody() : Collections.emptyList();
    }

    public List<DriverStandingDto> getDriverStandings() {
        ResponseEntity<List<DriverStandingDto>> response = restTemplate.exchange(
                flaskBaseUrl + "/standings/drivers",
                HttpMethod.GET,
                null,
                new ParameterizedTypeReference<List<DriverStandingDto>>() {}
        );
        return response.getBody() != null ? response.getBody() : Collections.emptyList();
    }

    public List<ConstructorStandingDto> getConstructorStandings() {
        ResponseEntity<List<ConstructorStandingDto>> response = restTemplate.exchange(
                flaskBaseUrl + "/standings/constructors",
                HttpMethod.GET,
                null,
                new ParameterizedTypeReference<List<ConstructorStandingDto>>() {}
        );
        return response.getBody() != null ? response.getBody() : Collections.emptyList();
    }

    public List<ChampionPredictionDto> getChampionPrediction() {
        ResponseEntity<List<ChampionPredictionDto>> response = restTemplate.exchange(
                flaskBaseUrl + "/predict/champion",
                HttpMethod.GET,
                null,
                new ParameterizedTypeReference<List<ChampionPredictionDto>>() {}
        );
        return response.getBody() != null ? response.getBody() : Collections.emptyList();
    }

    public List<RacePredictionDto> getRacePrediction(Integer raceId) {
        ResponseEntity<List<RacePredictionDto>> response = restTemplate.exchange(
                flaskBaseUrl + "/predict/race/" + raceId,
                HttpMethod.GET,
                null,
                new ParameterizedTypeReference<List<RacePredictionDto>>() {}
        );
        return response.getBody() != null ? response.getBody() : Collections.emptyList();
    }

    public ImportResponseDto importHistoricalData(Integer startYear, Integer endYear) {
        ImportRequestDto requestDto = new ImportRequestDto();
        requestDto.setStart_year(startYear);
        requestDto.setEnd_year(endYear);

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        HttpEntity<ImportRequestDto> request = new HttpEntity<>(requestDto, headers);

        ResponseEntity<ImportResponseDto> response = restTemplate.exchange(
                flaskBaseUrl + "/data/import",
                HttpMethod.POST,
                request,
                ImportResponseDto.class
        );

        return response.getBody();
    }
}