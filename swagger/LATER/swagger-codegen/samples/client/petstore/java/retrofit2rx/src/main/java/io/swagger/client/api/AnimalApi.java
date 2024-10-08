package io.swagger.client.api;

import io.swagger.client.CollectionFormats.*;

import rx.Observable;
import retrofit2.http.*;

import okhttp3.RequestBody;
import okhttp3.ResponseBody;

import io.swagger.client.model.Animal;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public interface AnimalApi {
  /**
   * Add a new animal to the store
   * 
   * @param body Animal object that needs to be added to the store (required)
   * @return Call&lt;Void&gt;
   */
  @Headers({
    "Content-Type:application/json"
  })
  @POST("animal")
  Observable<Void> addAnimal(
    @retrofit2.http.Body Animal body
  );

  /**
   * Deletes a animal
   * 
   * @param animalId Animal id to delete (required)
   * @param apiKey  (optional)
   * @return Call&lt;Void&gt;
   */
  @DELETE("animal/{animalId}")
  Observable<Void> deleteAnimal(
    @retrofit2.http.Path("animalId") Long animalId, @retrofit2.http.Header("api_key") String apiKey
  );

  /**
   * Find animal by ID
   * Returns a single animal
   * @param animalId ID of pet to return (required)
   * @return Call&lt;Animal&gt;
   */
  @GET("animal/{animalId}")
  Observable<Animal> getAnimalById(
    @retrofit2.http.Path("animalId") Long animalId
  );

  /**
   * Update an existing animal
   * 
   * @param body Animal object that needs to be added. (required)
   * @return Call&lt;Void&gt;
   */
  @Headers({
    "Content-Type:application/json"
  })
  @PUT("animal")
  Observable<Void> updateAnimal(
    @retrofit2.http.Body Animal body
  );

  /**
   * Updates a animal
   * 
   * @param animalId ID of animal that needs to be updated (required)
   * @param name  (optional)
   * @param status  (optional)
   * @return Call&lt;Void&gt;
   */
  @retrofit2.http.FormUrlEncoded
  @POST("animal/{animalId}")
  Observable<Void> updateAnimalWithForm(
    @retrofit2.http.Path("animalId") Long animalId, @retrofit2.http.Field("name") String name, @retrofit2.http.Field("status") String status
  );

}
