const currentUrl = window.location.href;
const currentParams = new URLSearchParams(window.location.search);

const currentPath = new URL(currentUrl).pathname;
const currentCategory = getSlug(); //lấy dc slug từ url
const currentPlanting = currentParams.get("planting"); //lấy dc value của planting = 
const currentOrder = currentParams.get("order") || "-price";

$(`ul.list-category > li[data-active="${currentCategory}"]`).addClass("active"); 
//gọi đến ul có class là list-category và gọi tiếp đến thẻ con li có data-active của nó để addClass()

$(`.list-planting-method > a > span[data-active="${currentPlanting}"]`).addClass("active");

$(`select#sort-product > option[data-active="${currentOrder}"]`).attr("selected", true);

$(`ul.main-nav > li > a[href="${currentPath}"]`).parent().addClass("active")

$(`ul.main-nav > li[data-active="${currentCategory}"]`).addClass("active")

$("#sort-product").change(function () {
  let selectedValue = $(this).val();
  window.location.href = selectedValue;
});

function getSlug() {
  // let pathname = new URL(currentUrl).pathname;
  let slug = currentPath.substring(1, currentPath.lastIndexOf(".html"));

  return slug;
}
