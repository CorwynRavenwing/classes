/**
 * NOTE: This class is auto generated by the swagger code generator program (3.0.35-SNAPSHOT).
 * https://github.com/swagger-api/swagger-codegen
 * Do not edit the class manually.
 */
package io.swagger.api;

import java.util.Map;
import io.swagger.model.Order;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.enums.ParameterIn;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.media.ArraySchema;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.security.SecurityRequirement;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RequestPart;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.bind.annotation.CookieValue;

import javax.validation.Valid;
import javax.validation.constraints.*;
import java.util.List;
import java.util.Map;

@Validated
public interface StoreApi {

    @Operation(summary = "Delete purchase order by ID", description = "For valid response try integer IDs with positive integer value.\\ \\ Negative or non-integer values will generate API errors", tags={ "store" })
    @ApiResponses(value = { 
        @ApiResponse(responseCode = "400", description = "Invalid ID supplied"),
        
        @ApiResponse(responseCode = "404", description = "Order not found") })
    @RequestMapping(value = "/store/order/{orderId}",
        method = RequestMethod.DELETE)
    ResponseEntity<Void> deleteOrder(@Min(1L)@Parameter(in = ParameterIn.PATH, description = "ID of the order that needs to be deleted", required=true, schema=@Schema(allowableValues={  }, minimum="1"
)) @PathVariable("orderId") Long orderId);


    @Operation(summary = "Returns pet inventories by status", description = "Returns a map of status codes to quantities", security = {
        @SecurityRequirement(name = "api_key")    }, tags={ "store" })
    @ApiResponses(value = { 
        @ApiResponse(responseCode = "200", description = "successful operation", content = @Content(mediaType = "application/json", array = @ArraySchema(schema = @Schema(implementation = Map.class)))) })
    @RequestMapping(value = "/store/inventory",
        produces = "application/json", 
        method = RequestMethod.GET)
    ResponseEntity<Map<String, Integer>> getInventory();


    @Operation(summary = "Find purchase order by ID", description = "For valid response try integer IDs with value >= 1 and <= 10.\\ \\ Other values will generated exceptions", tags={ "store" })
    @ApiResponses(value = { 
        @ApiResponse(responseCode = "200", description = "successful operation", content = @Content(mediaType = "application/json", schema = @Schema(implementation = Order.class))),
        
        @ApiResponse(responseCode = "400", description = "Invalid ID supplied"),
        
        @ApiResponse(responseCode = "404", description = "Order not found") })
    @RequestMapping(value = "/store/order/{orderId}",
        produces = "application/json", 
        method = RequestMethod.GET)
    ResponseEntity<Order> getOrderById(@Min(1L) @Max(10L) @Parameter(in = ParameterIn.PATH, description = "ID of pet that needs to be fetched", required=true, schema=@Schema(allowableValues={  }, minimum="1", maximum="10"
)) @PathVariable("orderId") Long orderId);


    @Operation(summary = "Place an order for a pet", description = "", tags={ "store" })
    @ApiResponses(value = { 
        @ApiResponse(responseCode = "200", description = "successful operation", content = @Content(mediaType = "application/json", schema = @Schema(implementation = Order.class))),
        
        @ApiResponse(responseCode = "400", description = "Invalid Order") })
    @RequestMapping(value = "/store/order",
        produces = "application/json", 
        consumes = "application/json",
        method = RequestMethod.POST)
    ResponseEntity<Order> placeOrder(@Parameter(in = ParameterIn.DEFAULT, description = "order placed for purchasing the pet", required=true, schema=@Schema()) @Valid @RequestBody Order body);

}

