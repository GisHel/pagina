$(document).on("ready",inicio);
function inicio()
{
	$("#Temas").on("click",transicion);
}
function transicion()
{
	var cambiosarti =
	{
		height: "auto",
		opacity: 1,
		width: "90%",
		margin: "0, 1%, 1%, 10em"
	};
	var cambiosCSS =
	{
		margin: 0,
		overflow: "hidden",
		padding:0,
		width: 0,
		height:0, 

	};
	var cambiofig =
	{
		margin: 0,
		overflow: "hidden",
		padding:0,
		width: 0,
		height: 0,		
	};
	
	$("#historia").css(cambiosCSS);
	$("#curvas").css(cambiofig);
	$("#articulos").css(cambiosarti);
}
function openVentana()
		{
		$(".ventana").slideDown("slow");
		}
function closeVentana()
		{
		$(".ventana").slideUp("fast");
		}