package io.swagger.client.api;

import io.swagger.client.CollectionFormats.*;

import io.reactivex.Observable;
import retrofit2.http.*;

import okhttp3.RequestBody;
import okhttp3.ResponseBody;

import io.swagger.client.model.AllPetsResponse;
import java.io.File;
import io.swagger.client.model.ModelApiResponse;
import io.swagger.client.model.Pet;
import io.swagger.client.model.SinglePetResponse;
import io.swagger.client.model.SubCategory;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public interface PetApi {
  /**
   * Add a new pet to the store
   * 
   * @param body Pet object that needs to be added to the store (required)
   * @return Call&lt;Void&gt;
   */
  @Headers({
    "Content-Type:application/json"
  })
  @POST("pet")
  Observable<Void> addPet(
    @retrofit2.http.Body Pet body
  );

  /**
   * Deletes a pet
   * 
   * @param petId Pet id to delete (required)
   * @param apiKey  (optional)
   * @return Call&lt;Void&gt;
   */
  @DELETE("pet/{petId}")
  Observable<Void> deletePet(
    @retrofit2.http.Path("petId") Long petId, @retrofit2.http.Header("api_key") String apiKey
  );

  /**
   * 
   * 
   * @param body  (optional)
   * @return Call&lt;ModelApiResponse&gt;
   */
  @Headers({
    "Content-Type:application/json"
  })
  @POST("pet/category")
  Observable<ModelApiResponse> doCategoryStuff(
    @retrofit2.http.Body SubCategory body
  );

  /**
   * Finds Pets by status
   * Multiple status values can be provided with comma separated strings
   * @param status Status values that need to be considered for filter (required)
   * @return Call&lt;List&lt;Pet&gt;&gt;
   */
  @GET("pet/findByStatus")
  Observable<List<Pet>> findPetsByStatus(
    @retrofit2.http.Query("status") List<String> status
  );

  /**
   * Finds Pets by tags
   * Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.
   * @param tags Tags to filter by (required)
   * @return Call&lt;List&lt;Pet&gt;&gt;
   */
  @GET("pet/findByTags")
  Observable<List<Pet>> findPetsByTags(
    @retrofit2.http.Query("tags") List<String> tags
  );

  /**
   * 
   * 
   * @return Call&lt;AllPetsResponse&gt;
   */
  @GET("allPets")
  Observable<AllPetsResponse> getAllPets();
    

  /**
   * Find pet by ID
   * Returns a single pet
   * @param petId ID of pet to return (required)
   * @return Call&lt;Pet&gt;
   */
  @GET("pet/{petId}")
  Observable<Pet> getPetById(
    @retrofit2.http.Path("petId") Long petId
  );

  /**
   * 
   * 
   * @return Call&lt;SinglePetResponse&gt;
   */
  @GET("randomPet")
  Observable<SinglePetResponse> getRandomPet();
    

  /**
   * Update an existing pet
   * 
   * @param body Pet object that needs to be added to the store (required)
   * @return Call&lt;Void&gt;
   */
  @Headers({
    "Content-Type:application/json"
  })
  @PUT("pet")
  Observable<Void> updatePet(
    @retrofit2.http.Body Pet body
  );

  /**
   * Updates a pet in the store with form data
   * 
   * @param petId ID of pet that needs to be updated (required)
   * @param name  (optional)
   * @param status  (optional)
   * @return Call&lt;Void&gt;
   */
  @retrofit2.http.FormUrlEncoded
  @POST("pet/{petId}")
  Observable<Void> updatePetWithForm(
    @retrofit2.http.Path("petId") Long petId, @retrofit2.http.Field("name") String name, @retrofit2.http.Field("status") String status
  );

  /**
   * uploads an image
   * 
   * @param petId ID of pet to update (required)
   * @param additionalMetadata  (optional)
   * @param file  (optional)
   * @return Call&lt;ModelApiResponse&gt;
   */
  @retrofit2.http.Multipart
  @POST("pet/{petId}/uploadImage")
  Observable<ModelApiResponse> uploadFile(
    @retrofit2.http.Path("petId") Long petId, @retrofit2.http.Part("additionalMetadata") String additionalMetadata, @retrofit2.http.Part("file\"; filename=\"file") RequestBody file
  );

}
